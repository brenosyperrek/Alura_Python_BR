import re

class TelefoneBr:
    def __init__(self, telefone) -> None:
        if self.valida_telefone(telefone):
            self.numero = telefone
        else:
            raise ValueError("Numero de telefone inválido!!!")

    def valida_telefone(self, telefone):
        padrao = '([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})'
        if re.findall(padrao,telefone):
            return True
        else:
            return False

    def formata_numero(self):
        padrao = '([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})'
        resposta = re.search(padrao, self.numero)
        numero_formatado = "+{}({}){}-{}".format(resposta.group(1),resposta.group(2),resposta.group(3),resposta.group(4))
        return numero_formatado
        
    def __str__(self) -> str:
        return self.formata_numero()

    