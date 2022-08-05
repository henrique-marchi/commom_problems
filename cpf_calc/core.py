def cpf_generate(cpf):
    if len(cpf) != 9:
        raise RuntimeError(
            "The CPF must contain only number without the 2 verification digits"
        )
    number_weights = [10, 9, 8, 7, 6, 5, 4, 3, 2]
    splitted_cpf = list(map(int, str(cpf)))
    multiply1 = []
    multiply2 = []

    for num1, num2 in zip(splitted_cpf, number_weights):
        multiply1.append((num1 * num2))

    sum1 = sum(multiply1)
    result1 = 11 - (sum1 % 11)

    if result1 >= 10:
        result1 = 0

    splitted_cpf.append(result1)
    number_weights.insert(0, 11)

    for num1, num2 in zip(splitted_cpf, number_weights):
        multiply2.append((num1 * num2))

    sum2 = sum(multiply2)
    result2 = 11 - (sum2 % 11)

    if result2 >= 10:
        result2 = 0

    splitted_cpf.append(result2)
    end_result = "".join(str(x) for x in splitted_cpf)

    return end_result


def cpf_validation(cpf):
    str(cpf)
    if len(cpf) != 11:
        raise RuntimeError("The CPF must contain only numbers(11)")

    if (
        str(cpf) == "11111111111"
        or str(cpf) == "22222222222"
        or str(cpf) == "33333333333"
        or str(cpf) == "44444444444"
        or str(cpf) == "55555555555"
        or str(cpf) == "66666666666"
        or str(cpf) == "77777777777"
        or str(cpf) == "88888888888"
        or str(cpf) == "99999999999"
        or str(cpf) == "00000000000"
    ):
        raise RuntimeError(f"Invalid CPF format: {cpf}")

    splitted_cpf = list(map(int, str(cpf)))
    del splitted_cpf[9]
    del splitted_cpf[9]
    splitted_cpf = "".join(str(x) for x in splitted_cpf)

    validated_cpf = cpf_generate(splitted_cpf)

    if cpf != validated_cpf:
        raise RuntimeError(f"Invalid CPF: {cpf}, valid CPF: {validated_cpf}")

    return True
