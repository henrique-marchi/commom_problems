from pydantic import validator

def cep_validator(
    cep: int
):

    @validator("cep")
    def validate_cep(cls, v):
        print(f'before validation: {v}')
        if v.lenght != 8:
            raise RuntimeError(f"CEP invalid")
        if " " in v or "-" in v or "." in v or "/" in v:
            raise RuntimeError(f"CEP must be only numbers")
        print(f'after validation: {v}')
        return v