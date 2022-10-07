from acesso_cep import BuscaEndereco
import requests

cep = 88030500

objeto_cep = BuscaEndereco(cep)
print(objeto_cep)

bairro, cidade, estado = objeto_cep.acessa_via_cep()
print(bairro)
print(cidade)
print(estado)
