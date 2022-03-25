# Cassandra Script

## CRIE UMA KEYSPACE CHAMADA Escola

## SELECIONANDO UMA KEYSPACE

    CREATE KEYSPACE "Escola" WITH replication = {'class':'SimpleStrategy', 'replication_factor':1};
    use "Escola";

## CRIANDO A TABELA ALUNO E COM CHAVE DE PARTICIONAMENTO = Materia

    create table aluno(
	    id int,
	    nome text,
	    materia text,
	    nota float,
	    falta int,
	    emails set<text>,
	    primary key (materia,id)
    );

## INSIRA 5 REGISTROS NA TABELA aluno

    INSERT INTO aluno(id, nome, materia, nota, falta, emails) VALUES(1, 'Fabio', 'Spark', 9.5, 0, {'fabio@escola.com'});
    INSERT INTO aluno(id, nome, materia, nota, falta, emails) VALUES(2, 'Joao', 'ML', 8, 1, {'joao@escola.com'});
    INSERT INTO aluno(id, nome, materia, nota, falta, emails) VALUES(3, 'Maria', 'Redes', 8.5, 2, {'maria@escola.com'});
    INSERT INTO aluno(id, nome, materia, nota, falta, emails) VALUES(4, 'Jose', 'Cassandra', 9, 3, {'jose@escola.com'});
    INSERT INTO aluno(id, nome, materia, nota, falta, emails) VALUES(5, 'Francisco', 'Computacao', 6, 0, {'francisco@escola.com'});

## ACRESCENTE 1 E-MAIL COMPLEMENTAR PARA 1 ALUNO

    update aluno SET emails = emails + {'joao2@escola.com'} where id = 2 and materia = 'ML';

## RETIRE O E-MAIL COMPLEMENTAR ADICIONADO NO EXERCICIO ANTERIOR

    update aluno SET emails = emails - {'joao2@escola.com'} where id = 2 and materia = 'ML';

##INSIRA 1 REGISTRO NA TABELA aluno COM TTL DE 1 HORA

    INSERT INTO aluno(id, nome, materia, nota, falta, emails) VALUES(6, 'Claudia', 'Spark', 8, 0, {'francisco@escola.com'}) USING TTL 3600;

## CRIE UM ARQUIVO CSV E IMPORTE MAIS 4 REGISTROS USANDO O COMPANDO COPY

    nano aluno.csv
    id,nome,materia,nota,falta,emails
    7,Israel,Spark,8.5,1,israel@escola.com
    8,Helder,Redes,7,2,helder@escola.com
    9,Vinicius,Cassandra,8,3,vinicius@escola.com
    10,Glauber,ML,9,4,glauber@escola.com

    COPY aluno(id, nome, materia, nota, falta, emails) from '/home/ambientelivre/Documentos/aluno.csv' WITH HEADER = TRUE;