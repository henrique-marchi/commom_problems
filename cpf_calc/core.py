def cpf_generate(cpf: str):
    splitted_cpf = list(cpf)

    for number in splitted_cpf:
        int(number)

    for number in splitted_cpf:
        print(type(number))


cpf = "42312465486"
print(cpf_generate(cpf))
