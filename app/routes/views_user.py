from flask import redirect,jsonify,request
from app.routes import main_bp
from app.models import db,Usuario
from passlib.hash import argon2
from datetime import datetime

@main_bp.route('/register', methods=['GET','POST'])
def register():

      data = request.json

      campos = ['nome','sobrenome','genero','nascimento',
            'cpf','telefone','estado','cidade','email','senha']

      if not data:
            return jsonify({'error': 'Nenhum campo foi preenchido'}), 400
    
      if all(campo in data and data[campo] for campo in campos):
            return jsonify({'error': 'Campos não preenchidos completamente'}), 400
      
      if Usuario.query.filter_by(email=data['email']).first():
            return jsonify({'error': 'Email já cadastrado'}), 400
        
      data['nome'] = f"{data['nome'].title()} {data['sobrenome'].title()}" 
      data.pop('sobrenome')

      data['senha_hash'] = argon2.hash(data['senha'])
      data.pop('senha')

      data['nascimento'] = datetime.strptime(data['nascimento'], "%Y-%m-%d").date()

      new_user = Usuario(**data)
      db.session.add(new_user)
      db.session.commit()

      return jsonify({'sucess': 'Usuário Registrado com Sucesso!'}),201