class Cep:
    cep: str

    def validate_cep(self):
        if len(self.cep) != 8:
            raise RuntimeError(f"CEP must contain only numbers")
