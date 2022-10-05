from validate_docbr import CPF, CNPJ

class CpfCnpj:
    
    def __init__(self, documento, tipo_documento) -> None:
        self.tipo_documento = tipo_documento
        documento = str(documento)
        if self.tipo_documento == 'cpf':
            if self.cpf_eh_valido(documento):
                self.cpf = documento
            else:
                raise ValueError("CPF Inválido")
        elif self.tipo_documento == 'cnpj':
            if self.cnpj_eh_valido(documento):
                self.cnpj = documento
            else:
                raise ValueError("CNPJ Inválido")
        else:
            raise ValueError('Documento inválido')

    def __str__(self) -> str:
        if self.tipo_documento == 'cpf':
            return self.format_cpf()
        elif self.tipo_documento == 'cnpj':
            return self.format_cnpj()
        
    def cpf_eh_valido(self, documento):
        if len(documento) == 11:
            validador = CPF()
            return validador.validate(documento)
        else:
            raise ValueError('Quantidade de dígitos inválida!')

    def format_cpf (self):
        mascara = CPF()
        return mascara.mask(self.cpf)        

    def cnpj_eh_valido (self, documento):
        if len(documento) == 14:
            validate_cnpj = CNPJ()
            return validate_cnpj.validate(documento)
        else:
            raise ValueError('Quantidade de digitos inválida')

    def format_cnpj (self):
        mascara = CNPJ()
        return mascara.mask(self.cnpj)        