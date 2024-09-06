-- DrillDown: Quadrimestre-mês e Estado → Cidades
SELECT 
    p.quarter AS quadrimestre,
    p.month AS mes,
    l.estado,
    l.cidade,
    SUM(v.valor_total) AS valor_total,
    SUM(v.unidades_total) AS quantidade_total
FROM vendas v
JOIN periodos p ON v.periodo_id = p.id
JOIN locais l ON v.local_id = l.id
GROUP BY p.quarter, p.month, l.estado, l.cidade
ORDER BY p.quarter, p.month, l.estado, l.cidade;

-- Rollup: Quadrimestre-mês e Estado → Cidades
SELECT 
    COALESCE(CAST(p.quarter AS VARCHAR), 'Total Geral') AS quadrimestre,
    COALESCE(CAST(p.month AS VARCHAR), 'Total Geral') AS mes,
    l.estado,
    l.cidade,
    SUM(v.valor_total) AS valor_total,
    SUM(v.unidades_total) AS quantidade_total
FROM vendas v
JOIN periodos p ON v.periodo_id = p.id
JOIN locais l ON v.local_id = l.id
GROUP BY ROLLUP(p.quarter, p.month, l.estado, l.cidade)
ORDER BY p.quarter, p.month, l.estado, l.cidade;

-- Dice: Filtro para vendas às quartas-feiras em todas as lojas
SELECT 
    p.quarter AS quadrimestre,
    p.month AS mes,
    l.estado,
    l.cidade,
    SUM(v.valor_total) AS valor_total,
    SUM(v.unidades_total) AS quantidade_total
FROM 
    vendas v
JOIN 
    periodos p ON v.periodo_id = p.id
JOIN 
    locais l ON v.local_id = l.id
WHERE 
    p.day_of_week = 'Quarta-Feira'
GROUP BY 
    p.quarter, p.month, l.estado, l.cidade
ORDER BY 
    p.quarter, p.month, l.estado, l.cidade;
