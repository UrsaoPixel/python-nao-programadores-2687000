# Criaremos um script que imprimirá na tela o total de horas que uma pessoa estudou durante um determinado período:

# 1. Crie uma variável chamada "nome" e, usando o método input(), atribua a ela um nome;
nome = input('Digite seu nome: ')

# 2. Crie uma variável chamada "total_dias" e, usando o método input(), solicite o total de dias dedicados ao estudo por semana;
total_dias = input('Insira quantos dias da semana pretende dedicar: ')

# 3. Crie uma variável chamada "total_horas" e, usanod o método input(), solicite a média de horas estudada por dia;
total_horas = input('Quantas horas por dia pretende estudar?: ')

# 4. Crie uma variável chamada "curso" e, usando o método input(), solicite o título do curso desejado;
curso = input ('Qual nome do curso ao qual vai se dedicar: ')

# 5. Imprima na tela uma frase informando o nome da estudante, o total_dias dedicados aos estudos, o total horas semanais e o curso.
total_dias = int(total_dias) 
total_horas = int(total_horas)

print (f'o estudante {nome}, vai dedicar um total de {total_dias} dias na semana, com uma média diaria de {total_horas} horas. Isso significa que você estuda {total_dias*total_horas} horas por semana para o curso {curso}.')
