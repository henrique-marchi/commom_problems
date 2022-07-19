from core import cpf_generate, cpf_validation

cpf = "567678435"
print(f"Generated CPF: {cpf_generate(cpf)}")
cpf = "45317828791"
print(f"Validated CPF: {cpf_validation(cpf)}")
