CREATE TABLE operadoras (
    id INT AUTO_INCREMENT PRIMARY KEY,
    Registro_ANS VARCHAR(50) NULL,
    CNPJ VARCHAR(50) NULL,
    Razao_Social VARCHAR(255) NULL,
    Nome_Fantasia VARCHAR(255) NULL,
    Modalidade VARCHAR(100) NULL,
    Logradouro VARCHAR(255) NULL,
    Numero VARCHAR(50) NULL,
    Complemento VARCHAR(255) NULL,
    Bairro VARCHAR(100) NULL,
    Cidade VARCHAR(100) NULL,
    UF CHAR(50) NULL,
    CEP VARCHAR(50) NULL,
    DDD VARCHAR(50) NULL,
    Telefone VARCHAR(50) NULL,
    Fax VARCHAR(50) NULL,
    Endereco_eletronico VARCHAR(255) NULL,
    Representante VARCHAR(255) NULL,
    Cargo_Representante VARCHAR(100) NULL,
    Regiao_de_Comercializacao VARCHAR(100) NULL,
    Data_Registro_ANS DATE NULL
);


CREATE TABLE `demonstracoes_contabeis` (
    `id` INT AUTO_INCREMENT PRIMARY KEY,
    `DATA` DATE,
    `REG_ANS` VARCHAR(20),
    `CD_CONTA_CONTABIL` VARCHAR(50),
    `DESCRICAO` VARCHAR(255),
    `VL_SALDO_INICIAL` DECIMAL(15,2),
    `VL_SALDO_FINAL` DECIMAL(15,2),
);


-- maiores despesas 2024
SELECT dc.REG_ANS, 
       op.Razao_Social, 
       SUM(CAST(dc.VL_SALDO_FINAL AS DECIMAL(15,2))) AS total_despesas
FROM demonstracoes_contabeis dc
JOIN operadoras op ON dc.REG_ANS = op.Registro_ANS
WHERE dc.DESCRICAO LIKE '%EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR %'
AND YEAR(dc.DATA) = 2024
GROUP BY dc.REG_ANS, op.Razao_Social
ORDER BY total_despesas DESC

-- top 10 despesas ultimo trimestre de 2024
SELECT dc.REG_ANS, 
       op.Razao_Social, 
       SUM(CAST(dc.VL_SALDO_FINAL AS DECIMAL(15,2))) AS total_despesas
FROM demonstracoes_contabeis dc
JOIN operadoras op ON dc.REG_ANS = op.Registro_ANS
WHERE dc.DESCRICAO LIKE '%EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR %'
AND YEAR(dc.DATA) = 2024
AND dc.DATA >= DATE_SUB(DATE_FORMAT(CURDATE(), '%Y-01-01'), INTERVAL 3 MONTH)
GROUP BY dc.REG_ANS, op.Razao_Social
ORDER BY total_despesas DESC
LIMIT 10;