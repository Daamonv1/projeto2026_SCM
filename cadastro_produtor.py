#Modulo de cadastro de produtor rural - AgroApp 2026

def cadastrar_produtor (nome, cpf, municipio, area_ha):

#Cadastra um novo produtor rural no sistema.

    produtor =  {

"nome": nome,
"cpf": cpf,
"municipio": municipio,
"area_ha": area_ha
}

    return produtor


print("Modulo de cadastro de produtor rural iniciado")