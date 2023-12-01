# Responder com queries:

## 1) Estudantes + créditos totais

### 1.1) Quantos estudantes estão com mais de 4 créditos? Responder com nome do aluno e quantidade de horas
```
MATCH (a:Aluno)-[:MATRICULADO]->(c:Disciplina)-[r:TRABALHO]->(p:Projeto)
WITH a, SUM(r.horas) AS horas_totais
WHERE horas_totais > 4
RETURN a.nome AS nome_aluno, horas_totais AS total_horas;

```

## 2) Disciplina por aluno
### 2.1) Disciplina com mais alunos matriculados ordenada
```
MATCH (a:Aluno)-[:MATRICULADO]->(c:Disciplina)
WITH c, COUNT(DISTINCT a) AS total_alunos
RETURN c.nome AS nome_disciplina, total_alunos
ORDER BY total_alunos DESC;

```

## 3) Alunos por sala de aula
### 3.1)Salas por % da capacidade 
```
MATCH (a:Aluno)-[:MATRICULADO]->()-[:ALOCADO]->(s:Sala)
WITH s, COUNT(DISTINCT a) AS total_alunos
RETURN s.nome AS nome_sala, total_alunos, toFloat(total_alunos) / s.capacidade AS percentual_capacidade
ORDER BY percentual_capacidade DESC;

```

## 4) Quantidade de alunos por blocos da faculdade (A,B,C)
```
MATCH (a:Aluno)-[:MATRICULADO]->()-[:ALOCADO]->(s:Sala)
RETURN s.bloco AS bloco, COUNT(DISTINCT a) AS total_alunos
ORDER BY bloco;

```