from datetime import datetime

class DatasBr:

    def __init__(self) -> None:
        self.momento_cadastro = datetime.today()

    def mes_cadastro(self):
        meses_do_ano = [
            "janeiro", "fevereiro", "março",
            "abril", "maio", "junho",
            "julho", "agosto", "setembro",
            "outubro", "novembro", "dezembro"
        ]
        mes_cadastro = self.momento_cadastro.month
        return meses_do_ano[mes_cadastro - 1]

    def dia_semana(self):
        dia_semana_lista = [
            "segunda-feira", "terça-feira",
            "quarta-feira", "quinta-feira", "sexta-feira",
            "sábado", "domingo"
        ]
        dia_semana = self.momento_cadastro.weekday()
        return dia_semana_lista[dia_semana]

