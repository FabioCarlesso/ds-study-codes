# Hbase Script

## 1) Criar um namespace com nome hospital.

    create_namespace 'hospital'

## 2) criar uma estrutura de dados para armazenas os seguintes dados.

    paciente (nome,cpf,rg, endereco residencia[rua,numero,bairro], endereco comercial[rua,numero,bairro])
    leito (numeroleito,data_entrada)
    cid ( codigo_da_cid , data_incidencia)

    create 'hospital:infoPaciente', 'paciente', 'endRes', 'endCom', 'leito', 'cid'

## 3) inserir 4 registro.

### 1 registro
    put 'hospital:infoPaciente', 1, 'paciente:nome', 'Fabio'
    put 'hospital:infoPaciente', 1, 'paciente:cpf', '06112332158'
    put 'hospital:infoPaciente', 1, 'paciente:rg', '80883332'
    put 'hospital:infoPaciente', 1, 'endRes:rua', 'Rua Minas Gerais'
    put 'hospital:infoPaciente', 1, 'endRes:numero', '545'
    put 'hospital:infoPaciente', 1, 'endRes:bairro', 'Centro'
    put 'hospital:infoPaciente', 1, 'endCom:rua', 'Rua do Mato Grosso'
    put 'hospital:infoPaciente', 1, 'endCom:numero', '1000'
    put 'hospital:infoPaciente', 1, 'endCom:bairro', 'Centro'
    put 'hospital:infoPaciente', 1, 'leito:numeroLeito', '8'
    put 'hospital:infoPaciente', 1, 'leito:dataEntrada', '13/11/2021'
    put 'hospital:infoPaciente', 1, 'cid:codCid', 'D840'
    put 'hospital:infoPaciente', 1, 'leito:dataIncidencia', '12/11/2021

### 2 registro
    put 'hospital:infoPaciente', 2, 'paciente:nome', 'Joao'
    put 'hospital:infoPaciente', 2, 'paciente:cpf', '06112332160'
    put 'hospital:infoPaciente', 2, 'paciente:rg', '80883335'
    put 'hospital:infoPaciente', 2, 'endRes:rua', 'Rua Belo Horizonte'
    put 'hospital:infoPaciente', 2, 'endRes:numero', '500'
    put 'hospital:infoPaciente', 2, 'endRes:bairro', 'Centro'
    put 'hospital:infoPaciente', 2, 'endCom:rua', 'Rua do Mato Grosso'
    put 'hospital:infoPaciente', 2, 'endCom:numero', '1000'
    put 'hospital:infoPaciente', 2, 'endCom:bairro', 'Centro'
    put 'hospital:infoPaciente', 2, 'leito:numeroLeito', '7'
    put 'hospital:infoPaciente', 2, 'leito:dataEntrada', '05/11/2021'
    put 'hospital:infoPaciente', 2, 'cid:codCid', 'D520'
    put 'hospital:infoPaciente', 2, 'leito:dataIncidencia', '04/11/2021

### 3 registro
    put 'hospital:infoPaciente', 3, 'paciente:nome', 'Maria'
    put 'hospital:infoPaciente', 3, 'paciente:cpf', '06112332101'
    put 'hospital:infoPaciente', 3, 'paciente:rg', '80883339'
    put 'hospital:infoPaciente', 3, 'endRes:rua', 'Rua Foz do Iguaçu'
    put 'hospital:infoPaciente', 3, 'endRes:numero', '10'
    put 'hospital:infoPaciente', 3, 'endRes:bairro', 'Centro'
    put 'hospital:infoPaciente', 3, 'endCom:rua', 'Rua do São Paulo'
    put 'hospital:infoPaciente', 3, 'endCom:numero', '50'
    put 'hospital:infoPaciente', 3, 'endCom:bairro', 'Centro'
    put 'hospital:infoPaciente', 3, 'leito:numeroLeito', '6'
    put 'hospital:infoPaciente', 3, 'leito:dataEntrada', '02/11/2021'
    put 'hospital:infoPaciente', 3, 'cid:codCid', 'D600'
    put 'hospital:infoPaciente', 3, 'leito:dataIncidencia', '01/11/2021

### 4 registro
    put 'hospital:infoPaciente', 4, 'paciente:nome', 'Jose'
    put 'hospital:infoPaciente', 4, 'paciente:cpf', '06662332158'
    put 'hospital:infoPaciente', 4, 'paciente:rg', '80883346'
    put 'hospital:infoPaciente', 4, 'endRes:rua', 'Rua Santos'
    put 'hospital:infoPaciente', 4, 'endRes:numero', '655'
    put 'hospital:infoPaciente', 4, 'endRes:bairro', 'Centro'
    put 'hospital:infoPaciente', 4, 'endCom:rua', 'Rua do Paraná'
    put 'hospital:infoPaciente', 4, 'endCom:numero', '687'
    put 'hospital:infoPaciente', 4, 'endCom:bairro', 'Centro'
    put 'hospital:infoPaciente', 4, 'leito:numeroLeito', '5'
    put 'hospital:infoPaciente', 4, 'leito:dataEntrada', '25/10/2021'
    put 'hospital:infoPaciente', 4, 'cid:codCid', 'D840'
    put 'hospital:infoPaciente', 4, 'leito:dataIncidencia', '24/10/2021

## 4) atualizar o endereco comercial.

    put 'hospital:infoPaciente', 1, 'endCom:rua', 'Rua do Paraguai'
    put 'hospital:infoPaciente', 1, 'endCom:numero', '789'
    put 'hospital:infoPaciente', 1, 'endCom:bairro', 'Jardim Sao Paulo'

## 5) listar/mostrar os dados de 1 registro 

    get 'hospital:infoPaciente', 1

## 6) deletar a familia de endereco residencial de um registro.

    delete 'hospital:infoPaciente', 1, 'endRes:rua'
    delete 'hospital:infoPaciente', 1, 'endRes:numero'
    delete 'hospital:infoPaciente', 1, 'endRes:bairro'

# 7) deletar um registro total.

    deleteall 'hospital:infoPaciente', 1