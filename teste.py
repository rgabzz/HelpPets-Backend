data = {'nome': 'A',
        'sobrenome': 'A',
        'genero': 'A',
        'nascimento': 'A',
        'cpf': 'A',
        'telefone': 'A',
        'estado': 'A',
        'cidade': 'A',
        'email': 'A',
        'senha': 'A'}

campos = ['nome','sobrenome','genero','nascimento',
            'cpf','telefone','estado','cidade','email','senha']

coot= 1
for campo in campos:
    if campo in data and data[campo]:
        print('Sucess!', coot) 
        coot += 1