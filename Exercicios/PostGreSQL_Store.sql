--2. Fazer uma operação de DRILL-DOWN
   -- 1. Soma de vendas por marca e por segmento

SELECT
    dm.marca AS Marca,
    ds.segmento AS Segmento,
    SUM(fv.quantidade) AS Total_Vendas
FROM
    fato_vendas fv (NOLOCK)
JOIN
    dim_marca dm ON fv.id_marca = dm.id
JOIN
    dim_segmento ds ON fv.id_segmento = ds.id
GROUP BY
    dm.marca, ds.segmento
ORDER BY
    dm.marca, ds.segmento;


--Operação de ROLL-UP:
  --Soma de vendas Por País > Marca:
SELECT
    dp.pais AS Pais,
    dm.marca AS Marca,
    SUM(fv.quantidade) AS Total_Vendas
FROM
    fato_vendas fv (NOLOCK)
JOIN
    dim_marca dm ON fv.id_marca = dm.id
JOIN
    dim_pais dp ON dm.id_pais = dp.id
GROUP BY
    dp.pais, dm.marca
ORDER BY
    dp.pais, dm.marca;

  --Soma de vendas Por Semana > Dia:
SELECT
    dt.no_semana_ano AS Semana,
    dt.dia AS Dia,
    SUM(fv.quantidade) AS Total_Vendas
FROM
    fato_vendas fv (NOLOCK)
JOIN
    dim_tempo dt ON fv.id_tempo = dt.id
GROUP BY
    dt.no_semana_ano, dt.dia
ORDER BY
    dt.no_semana_ano, dt.dia;


--Operação de SLICE:
  --Cortar por Nike:
SELECT
    dm.marca AS Marca,
    ds.segmento AS Segmento,
    SUM(fv.quantidade) AS Total_Vendas
FROM
    fato_vendas fv (NOLOCK)
JOIN
    dim_marca dm ON fv.id_marca = dm.id
JOIN
    dim_segmento ds ON fv.id_segmento = ds.id
WHERE
    dm.marca LIKE 'Nike'
GROUP BY
    dm.marca, ds.segmento;

    
--Operação de DICE:
  --Cortar por País = Japão, Semana = 44:
  SELECT
    dp.pais AS Pais,
    dt.no_semana_ano AS Semana,
    dm.marca AS Marca,
    SUM(fv.quantidade) AS Total_Vendas
FROM
    fato_vendas fv (NOLOCK)
JOIN
    dim_marca dm ON fv.id_marca = dm.id
JOIN
    dim_pais dp ON dm.id_pais = dp.id
JOIN
    dim_tempo dt ON fv.id_tempo = dt.id
WHERE
    dp.pais LIKE 'Japão' AND dt.no_semana_ano = 44
GROUP BY
    dp.pais, dt.no_semana_ano, dm.marca;


--Operação de PIVOT:
  --Soma do total de vendas onde as colunas são as marcas e as linhas são dias-da-semana:
SELECT
    dt.dia_semana AS "Dia da Semana",
    SUM(CASE WHEN dm.marca = 'Adidas' THEN fv.quantidade ELSE 0 END) AS Adidas,
    SUM(CASE WHEN dm.marca = 'Asics' THEN fv.quantidade ELSE 0 END) AS Asics,
    SUM(CASE WHEN dm.marca = 'Fila' THEN fv.quantidade ELSE 0 END) AS Fila,
    SUM(CASE WHEN dm.marca = 'Mizuno' THEN fv.quantidade ELSE 0 END) AS Mizuno,
    SUM(CASE WHEN dm.marca = 'New Balance' THEN fv.quantidade ELSE 0 END) AS New_Blance,
    SUM(CASE WHEN dm.marca = 'Rainha' THEN fv.quantidade ELSE 0 END) AS Rainha,
    SUM(CASE WHEN dm.marca = 'Olympikus' THEN fv.quantidade ELSE 0 END) AS Olympikus
FROM
    fato_vendas fv (NOLOCK)
JOIN
    dim_marca dm ON fv.id_marca = dm.id
JOIN
    dim_tempo dt ON fv.id_tempo = dt.id
GROUP BY
    dt.dia_semana
ORDER BY
    dt.dia_semana;
