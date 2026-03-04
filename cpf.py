def validar_cpf(cpf):
   if not cpf.isdigit():
        return 'CPF deve conter apenas números.'
   if len(cpf) != 11:
        return 'CPF deve conter exatamente 11 dígitos.'
   return 'CPF válido.'    

cpf_input = input("Digite o CPF (apenas números): ")
print(validar_cpf(cpf_input))   