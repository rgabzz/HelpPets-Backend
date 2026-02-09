from flask import redirect,jsonify,request
from flask_jwt_extended import create_access_token,jwt_required, get_jwt_identity
from app.routes.user import user_bp
from app.models import db,Usuarios
from passlib.hash import argon2
from datetime import datetime

@user_bp.route('/me',methods=['GET'])
@jwt_required()
def me():
      user_id = get_jwt_identity()

      user = Usuarios.query.get(user_id)
      if not user:
            return jsonify({'error': 'Usuário não encontrado'}), 404

      return jsonify({'nome': user.nome, 'email': user.email, 'cargo': user.tipo})

@user_bp.route('/register', methods=['POST'])
def register():
      data = request.get_json()

      campos = ['nome','sobrenome','genero','nascimento',
            'cpf','telefone','estado','cidade','email','senha']

      if not data:
            return jsonify({'error': 'Nenhum campo foi preenchido'}), 400
    
      if not all(campo in data and data[campo] for campo in campos):
            return jsonify({'error': 'Campos não preenchidos completamente'}), 400
      
      if Usuarios.query.filter_by(email=data['email']).first():
            return jsonify({'error': 'Email já cadastrado'}), 400
        
      data['nome'] = f"{data['nome'].title()} {data['sobrenome'].title()}" 
      data.pop('sobrenome')

      data['senha_hash'] = argon2.hash(data['senha'])
      data.pop('senha')

      data['nascimento'] = datetime.strptime(data['nascimento'], "%Y-%m-%d").date()

      new_user = Usuarios(**data)
      db.session.add(new_user)
      db.session.commit()

      return jsonify({'sucess': 'Usuário Registrado com Sucesso!'}),201

@user_bp.route('/login', methods=['POST'])
def login():
      data = request.get_json()
      campos = ['email','senha']

      if not data:
            return jsonify({'error': 'Nenhum campo foi preenchido'}), 400
      
      if not all(campo in data and data[campo] for campo in campos):
            return jsonify({'error': 'Campos não preenchidos completamente'}), 400
      
      user = Usuarios.query.filter_by(email=data['email']).first()

      if not user or not argon2.verify(data['senha'],user.senha_hash):
            return jsonify({'error': 'Credenciais inválidas'}), 401
      
      if not user.ativo:
            return jsonify({'error': 'Conta desativada pelos desenvolvedores'}), 403

      token = create_access_token(identity=user.id)      

      return jsonify({'access_token': token, 'Sucess':'Usuario Logado com Sucesso!'}),200
      



