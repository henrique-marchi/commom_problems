import re


def validate_cep(cep: str):
    regex = re.compile("[@_!#$%^&*() <>?/\|}{~:]")
    testcep = cep
    if len(testcep) != 8:
        raise RuntimeError(f"CEP must contain only numbers")
    if regex.search(testcep) != None:
        raise RuntimeError(f"CEP must contain only numbers")
    try:
        int(testcep)
    except:
        raise RuntimeError(f"CEP must contain only numbers")

    return testcep
