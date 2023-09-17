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

# Executar os comandos SQL para criar as tabelas
try:
    # Comandos SQL para criar as tabelas (mesmo código que você forneceu)
    create_tables = """
        DROP TABLE IF EXISTS fato_vendas CASCADE;
        DROP TABLE IF EXISTS dim_pais CASCADE;
        DROP TABLE IF EXISTS dim_marca CASCADE;
        DROP TABLE IF EXISTS dim_tempo CASCADE;
        DROP TABLE IF EXISTS dim_segmento CASCADE;

        CREATE TABLE dim_tempo (
            id SERIAL PRIMARY KEY,
            dia INT NOT NULL,
            mes INT NOT NULL,
            ano INT NOT NULL,
            dia_semana VARCHAR NOT NULL,
            no_semana_ano INT NOT NULL
        );

        CREATE TABLE dim_segmento (
            id SERIAL PRIMARY KEY,
            segmento VARCHAR NOT NULL
        );

        CREATE TABLE dim_pais (
            id SERIAL PRIMARY KEY,
            pais VARCHAR NOT NULL
        );

        CREATE TABLE dim_marca (
            id SERIAL PRIMARY KEY,
            marca VARCHAR NOT NULL,
            id_pais INT NOT NULL,
            FOREIGN KEY (id_pais) REFERENCES dim_pais(id)
        );

        CREATE TABLE fato_vendas (
            id_marca INT NOT NULL,
            id_segmento INT NOT NULL,
            quantidade INT NOT NULL,
            id_tempo INT NOT NULL,
            PRIMARY KEY (id_marca, id_segmento, id_tempo),
            FOREIGN KEY (id_marca) REFERENCES dim_marca(id),
            FOREIGN KEY (id_segmento) REFERENCES dim_segmento(id),
            FOREIGN KEY (id_tempo) REFERENCES dim_tempo(id)
        );
    """

    # Executar os comandos SQL
    cursor.execute(create_tables)
    conn.commit()
    print("Tabelas criadas com sucesso!")
except Exception as e:
    conn.rollback()
    print(f"Erro ao criar tabelas: {e}")
finally:
    cursor.close()
    conn.close()
