import psycopg2
from urllib.parse import urlparse

# URL de conexão
url = "postgres://jktyatpd:password@silly.db.elephantsql.com/jktyatpd"

# Parse a URL
url_parts = urlparse(url)

# Estabelecer a conexão
try:
    conn = psycopg2.connect(
        database=url_parts.path[1:],
        user=url_parts.username,
        password=url_parts.password,
        host=url_parts.hostname,
        port=url_parts.port
    )
    cursor = conn.cursor()
except Exception as e:
    print(f"Erro ao conectar ao banco de dados: {e}")

# Inserir dados nas tabelas
try:
    # Inserir dados na tabela dim_pais
    cursor.execute("""
        INSERT INTO dim_pais (id, pais)
        OVERRIDING SYSTEM VALUE
        VALUES
        (1, 'Brasil'), (2, 'Europa'), (3, 'Estados Unidos'), (4, 'Japão');
    """)

    # Inserir dados na tabela dim_marca
    cursor.execute("""
        INSERT INTO dim_marca (id, marca, id_pais)
        OVERRIDING SYSTEM VALUE
        VALUES
        (1, 'New Balance', 3),
        (2, 'Nike', 3),
        (3, 'Adidas', 2),
        (4, 'Fila', 2),
        (5, 'Rainha', 1),
        (6, 'Mizuno', 4),
        (7, 'Asics', 4),
        (8, 'Olympikus', 1);
    """)

    # Inserir dados na tabela dim_segmento
    cursor.execute("""
        INSERT INTO dim_segmento (id, segmento)
        OVERRIDING SYSTEM VALUE
        VALUES
        (1, 'Corrida'),
        (2, 'Treino'),
        (3, 'Futebol'),
        (4, 'Casual'),
        (5, 'Skate'),
        (6, 'Basquete');
    """)
# Inserir dados na tabela dim_tempo
    cursor.execute("""
        INSERT INTO dim_tempo (id, dia, dia_semana, mes, ano, no_semana_ano)
        OVERRIDING SYSTEM VALUE
        VALUES
        (1,  1, 'Quarta-feira', 11, 2023, 44),
        (2,  2, 'Quinta-feira', 11, 2023, 44),
        (3,  3, 'Sexta-feira', 11, 2023, 44),
        (4,  4, 'Sábado', 11, 2023, 44),
        (5,  5, 'Domingo', 11, 2023, 44),
        (6,  6, 'Segunda-feira', 11, 2023, 45),
        (7,  7, 'Terça-feira', 11, 2023, 45),
        (8,  8, 'Quarta-feira', 11, 2023, 45),
        (9,  9, 'Quinta-feira', 11, 2023, 45),
        (10, 10, 'Sexta-feira', 11, 2023, 45),
        (11, 11, 'Sábado', 11, 2023, 45),
        (12, 12, 'Domingo', 11, 2023, 45),
        (13, 13, 'Segunda-feira', 11, 2023, 46),
        (14, 14, 'Terça-feira', 11, 2023, 46),
        (15, 15, 'Quarta-feira', 11, 2023, 46),
        (16, 16, 'Quinta-feira', 11, 2023, 46),
        (17, 17, 'Sexta-feira', 11, 2023, 46),
        (18, 18, 'Sábado', 11, 2023, 46),
        (19, 19, 'Domingo', 11, 2023, 46),
        (20, 20, 'Segunda-feira', 11, 2023, 47),
        (21, 21, 'Terça-feira', 11, 2023, 47),
        (22, 22, 'Quarta-feira', 11, 2023, 47),
        (23, 23, 'Quinta-feira', 11, 2023, 47),
        (24, 24, 'Sexta-feira', 11, 2023, 47),
        (25, 25, 'Sábado', 11, 2023, 47),
        (26, 26, 'Domingo', 11, 2023, 47),
        (27, 27, 'Segunda-feira', 11, 2023, 48),
        (28, 28, 'Terça-feira', 11, 2023, 48),
        (29, 29, 'Quarta-feira', 11, 2023, 48),
        (30, 30, 'Quinta-feira', 11, 2023, 48);
    """)
    #Dia 01
    cursor.execute("""
        INSERT INTO fato_vendas (id_marca, id_segmento, quantidade, id_tempo)
        VALUES
        (1, 4, 25, 1),
        (2, 5, 34, 1),
        (3, 1, 23, 1),
        (4, 6, 54, 1),
        (5, 3, 40, 1),
        (6, 2, 29, 1),
        (7, 1, 50, 1),
        (8, 4, 37, 1),
        (1, 1, 41, 1),
        (2, 2, 36, 1),
        (3, 3, 9, 1),
        (4, 5, 7, 1),
        (5, 6, 15, 1),
        (6, 3, 10, 1),
        (7, 3, 8, 1),
        (8, 5, 11, 1);
    """)
    
    cursor.execute("DELETE FROM fato_vendas;")

    conn.commit()
    print("Dados inseridos na tabela dim_tempo com sucesso!")
except Exception as e:
    conn.rollback()
    print(f"Erro ao inserir dados na tabela dim_tempo: {e}")

finally:
    cursor.close()
    conn.close()
