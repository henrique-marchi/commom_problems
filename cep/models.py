def validate_cep(cep):
    cep = str(cep)

    if len(cep) != 8:
        raise RuntimeError(f"CEP must contain only numbers")
    return cep
