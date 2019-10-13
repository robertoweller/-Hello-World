documento = open('doc.txt','w')

for q in range(1, 30):
	documento.write('''
------------------------------------------
{}.

Nome: 

Idade: 

CPF: 

RG: 

Data nasc: 

Signo: 

Mae: 

Pai: 

Email: 

Senha: 

Cep: 

Endereco: 

Numero: 

Bairro: 

Cidade: 

Estado:

Telefone fixo: 

Celular: 

Altura: 

Peso: 

Tipo Saguineo: 

Cor: 

------------------------------------------
	'''.format(q))

documento.close()
