from cpf_cnpj import Documento


numero_cnpj = '35379838000112'
numero_cpf = '90219899991'
documento = Documento.cria_documento(numero_cnpj)
print (documento)
