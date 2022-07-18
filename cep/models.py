from pydantic import validator

class Cep():
    cep: int

    @validator("cep")
    def validate_cep(cls, v):
        if cep.lenght != 8:
            raise RuntimeError(f"CEP invalid")
        if " " in cep or "-" in cep or "." in cep:
            raise RuntimeError(f"CEP must be only numbers")
        return 