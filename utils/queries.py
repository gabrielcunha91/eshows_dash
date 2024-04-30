

GET_VIEW_FATURAM_ESHOWS = """
SELECT
vfe.*,
tgdc.NOME as 'Grupo',
tke.KEYACCOUNT as 'KeyAccount',
to2.NOME as 'Operador'
FROM View_Faturam_Eshows vfe
INNER JOIN T_COMPANIES tc ON (vfe.c_ID = tc.ID)
LEFT JOIN T_GRUPOS_DE_CLIENTES tgdc ON (tc.FK_GRUPO = tgdc.ID)
LEFT JOIN T_KEYACCOUNT_ESTABELECIMENTO tke ON (tc.FK_KEYACCOUNT = tke.ID)
LEFT JOIN T_OPERADORES to2 ON (tc.FK_OPERADOR = to2.ID)
WHERE vfe.`Data` > '2023-01-01 00:00:00'
ORDER BY vfe.`Data`, vfe.Casa  
"""

GET_CUSTOS_INTERNOS = """
SELECT
	tcie.ID as 'ID_Despesa',
	"T_CUSTOS_INTERNOS" as 'Tabela_Origem',
    tcie.DESCRICAO AS Descricao_da_Despesa,
    tcp.DESCRICAO AS Classificacao_Primaria,
    tcp.ID AS ID_Classificacao_Primaria,
    tcdc.DESCRICAO AS Centro_de_Custo,
    tcdc2.DESCRICAO AS Categoria_de_Custo,
    tcdc2.ID AS ID_Categoria,
    tcie.DATA_COMPETENCIA AS Data_Vencimento,
    tcie.VALOR AS Valor,
    CAST(CONCAT(YEAR(tcie.DATA_COMPETENCIA), '-', MONTH(tcie.DATA_COMPETENCIA), '-', '01') AS DATE) AS Primeiro_Dia_Mes_Vencimento
FROM T_CUSTOS_INTERNOS_ESHOWS tcie
LEFT JOIN T_CENTROS_DE_CUSTOS tcdc ON (tcie.FK_CENTRO_DE_CUSTO = tcdc.ID)
LEFT JOIN T_CLASSIFICACAO_PRIMARIA tcp ON (tcie.FK_CLASSIFICACAO_PRIMARIA = tcp.ID)
LEFT JOIN T_CATEGORIAS_DE_CUSTO tcdc2 ON (tcp.FK_CATEGORIA_CUSTO = tcdc2.ID)
WHERE
    ((tcie.DATA_VENCIMENTO > '2022-12-31 23:59:59')
        AND (tcie.TAG_INVESTIMENTO <> 1)
            AND (tcie.TAG_ESTORNO <> 1))
"""

GET_CUSTOS_COLABORADORES = """
SELECT
	tcce.ID as 'ID_Despesa',
	"T_CUSTOS_COLABORADORES_ESHOWS" as 'Tabela_Origem',
    CONCAT(tcdc.DESCRICAO, ' - ', tcp.DESCRICAO) AS Descricao_da_Despesa,
    tcp.DESCRICAO AS Classificacao_Primaria,
    tcp.ID AS ID_Classificacao_Primaria,
    tcdc.DESCRICAO AS Centro_de_Custo,
    tcdc2.DESCRICAO AS Categoria_de_Custo,
    tcdc2.ID AS ID_Categoria,
    tcce.DATA_VENCIMENTO AS Data_Vencimento,
    tcce.VALOR AS Valor,
    CAST(CONCAT(YEAR(tcce.DATA_VENCIMENTO), '-', MONTH(tcce.DATA_VENCIMENTO), '-', '01') AS DATE) AS Primeiro_Dia_Mes_Vencimento
FROM T_CUSTOS_COLABORADORES_ESHOWS tcce
JOIN T_COLABORADORES_ESHOWS tce ON (tcce.FK_COLABORADOR = tce.ID)
LEFT JOIN T_CENTROS_DE_CUSTOS tcdc ON (tcce.FK_CENTRO_DE_CUSTO = tcdc.ID)
LEFT JOIN T_CLASSIFICACAO_PRIMARIA tcp ON (tcce.FK_CLASSIFICACAO_PRIMARIA = tcp.ID)
LEFT JOIN T_CATEGORIAS_DE_CUSTO tcdc2 ON (tcp.FK_CATEGORIA_CUSTO = tcdc2.ID)
"""

GET_CUSTOS_PESSOAL = """
SELECT
tcpp.ID as 'ID_Despesa',
"T_CUSTOS_PESSOAL" as 'Tabela_Origem',
CONCAT(tcdc.DESCRICAO, ' - ', tcp.DESCRICAO) AS Descricao_da_Despesa,
tcp.DESCRICAO AS Classificacao_Primaria,
tcp.ID AS ID_Classificacao_Primaria,
tcdc.DESCRICAO AS Centro_de_Custo,
tcdc2.DESCRICAO AS Categoria_de_Custo,
tcdc2.ID AS ID_Categoria,
tcpp.DATA_VENCIMENTO AS Data_Vencimento,
tcpp.VALOR AS Valor,
CAST(CONCAT(YEAR(tcpp.DATA_VENCIMENTO), '-', MONTH(tcpp.DATA_VENCIMENTO), '-', '01') AS DATE) AS Primeiro_Dia_Mes_Vencimento
FROM T_CUSTOS_PESSOAL tcpp 
LEFT JOIN T_CENTROS_DE_CUSTOS tcdc ON (tcpp.CENTRO_DE_CUSTO = tcdc.ID)
LEFT JOIN T_CLASSIFICACAO_PRIMARIA tcp ON (tcpp.CLASSIFICACAO_PRIMARIA = tcp.ID)
LEFT JOIN T_CATEGORIAS_DE_CUSTO tcdc2 ON (tcp.FK_CATEGORIA_CUSTO = tcdc2.ID)
"""

