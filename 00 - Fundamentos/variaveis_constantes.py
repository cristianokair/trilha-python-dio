nome = "Guilherme"
idade = 28

nome, idade = "Giovanna", 27

print(nome, idade)

limite_saque_diario = 1000

BRAZILIAN_STATES = ["SP", "RJ", "SC", "RS"]

print(BRAZILIAN_STATES)

str2 = "120, 150, 170, 130, 200, 250, 180, 220, 210, 160, 140, 190"
teste = str2.split(",")
mapteste = list(map(int, teste))
print(mapteste)

soma = sum(mapteste)
print(soma)

list(map(lambda x: x*x, range(10)))