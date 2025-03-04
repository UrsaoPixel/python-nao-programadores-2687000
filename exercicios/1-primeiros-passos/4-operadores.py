ano_nascimento = 1989
ano_formatura = 2010

# Considerando que as variáveis acima correspondem a 'Gerlaine', descubra a idade dela no ano da sua formatura
formacao = (ano_formatura - ano_nascimento)
print(formacao)

# Escreva expressões comparativas usando os operadores relacionais >, <= e ==. Imprima na tela as respostas
a = ano_nascimento < ano_formatura
b = ano_formatura >= ano_nascimento
c = ano_nascimento == ano_formatura

print(a, b, c)

# Crie expressões comparativas mais complexas utilizando operadores lógicos and, or e not. Imprima na tela as respostas
x = ano_formatura and ano_formatura <= 2022
y = ano_formatura <= 2005

print(x, y, z)