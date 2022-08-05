import re


class Cep:
    cep: str

    def validate_cep(self):
        regex = re.compile("[@_!#$%^&*() <>?/\|}{~:]")
        testcep = self.cep
        if len(testcep) != 8:
            raise RuntimeError(f"CEP must contain only numbers")
        if regex.search(testcep) != None:
            raise RuntimeError(f"CEP must contain only numbers")
        try:
            int(testcep)
        except ValueError:
            raise RuntimeError(f"CEP must contain only numbers")
