import scrapy
import pandas as pd

class PokemondbSpider(scrapy.Spider):
    name = "pokemondb"
    allowed_domains = ["pokemondb.net"]
    start_urls = ["https://pokemondb.net/pokedex/all"]

        
    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36',
        'DOWNLOAD_DELAY': 0.2,  # Aumenta o delay para garantir que o servidor processe as requisições corretamente
        'RETRY_ENABLED': True,
        'RETRY_TIMES': 2,
        'RETRY_HTTP_CODES': [500, 502, 503, 504, 408],
        'LOG_LEVEL': 'DEBUG',
    }

    # Dicionário de cache para habilidades já processadas
    ability_cache = {}
    # Lista para acumular os dados de todos os Pokémon
    all_pokemon_data = []

    def parse(self, response):
        pokemons = response.css('table#pokedex tbody tr')
        for pokemon in pokemons:
            profile_link = pokemon.css("td:nth-child(2) a::attr(href)").get()
            if profile_link:
                profile_link = response.urljoin(profile_link)
                yield scrapy.Request(profile_link, callback=self.parse_profile)

    def parse_profile(self, response):
        name = response.css('h1::text').get()
        number = response.css('strong::text').get()
        types = response.css('tr:contains("Type") td a::text').getall()
        species = response.css('table.vitals-table tbody tr:nth-child(3)>td::text').get()
        height = response.css('table.vitals-table tbody tr:nth-child(4)>td::text').get()
        weight = response.css('table.vitals-table tbody tr:nth-child(5)>td::text').get()

        # Limpeza dos valores de altura e peso usando pandas
        height = pd.Series([height]).str.replace(r'\s*\(.*?\)\s*', '', regex=True).str.strip()[0]
        weight = pd.Series([weight]).str.replace(r'\s*\(.*?\)\s*', '', regex=True).str.strip()[0]

        # Extração das evoluções com nome, número e URL
        evolutions = []
        evo_elements = response.css('div.infocard-list-evo div.infocard')
        for evo in evo_elements:
            evo_name = evo.css('a.ent-name::text').get()
            evo_number = evo.css('small::text').get()
            evo_link = response.urljoin(evo.css('a.ent-name::attr(href)').get())
            
            evolutions.append({
                'name': evo_name,
                'number': evo_number.strip('#'),
                'url': evo_link
            })

        # Extração dos links das habilidades
        abilities_links = response.css('tr:contains("Abilities") td a::attr(href)').getall()

        # Inicializar a lista de habilidades vazia
        abilities = []

        # Construir o dicionário básico de dados do Pokémon
        pokemon_data = {
            'profile_link': response.url,
            'name': name,
            'number': number.strip('#'),
            'types': types,
            'species': species,
            'height': height,
            'weight': weight,
            'evolution': evolutions if evolutions else f"{name} does not evolve.",
            'abilities': abilities
        }

        # Caso não haja habilidades, adicionar diretamente à lista
        if not abilities_links:
            self.all_pokemon_data.append(pokemon_data)
        else:
            # Para cada link de habilidade, verificar se já está no cache
            for link in abilities_links:
                ability_url = response.urljoin(link)
                if ability_url in self.ability_cache:
                    # Se a habilidade já estiver no cache, usar diretamente
                    abilities.append(self.ability_cache[ability_url])
                    # Verifica se todas as habilidades foram processadas
                    if len(abilities) == len(abilities_links):
                        self.all_pokemon_data.append(pokemon_data)
                else:
                    # Se não estiver no cache, faz a requisição
                    request = scrapy.Request(ability_url, callback=self.parse_ability)
                    request.meta['pokemon_data'] = pokemon_data
                    request.meta['abilities_links'] = abilities_links
                    request.meta['ability_url'] = ability_url
                    yield request

    def parse_ability(self, response):
        # Extração do nome e descrição da habilidade
        ability_name = response.css('h1::text').get()
        ability_description = response.xpath('//p').xpath('string(.)').get()

        # Recuperação do dicionário pokemon_data da resposta anterior
        pokemon_data = response.meta['pokemon_data']
        ability_url = response.meta['ability_url']

        # Criar o dicionário da habilidade
        ability_data = {
            'name': ability_name,
            'description': ability_description
        }

        # add a habilidade a lista de habilidades
        pokemon_data['abilities'].append(ability_data)

        # add a habilidade ao cache
        self.ability_cache[ability_url] = ability_data

        # Verifica habilidades
        if len(pokemon_data['abilities']) == len(response.meta['abilities_links']):
            self.all_pokemon_data.append(pokemon_data)

    def close(self, reason):
        # Converte a lista de dados de Pokémon em um DataFrame do pandas
        df = pd.DataFrame(self.all_pokemon_data)
        
        with open('pokemon_data.json', 'w', encoding='utf-8') as f:
            f.write('[\n') 
            
            # Itera sobre cada linha do DataFrame e converte para JSON
            for index, row in df.iterrows():
                json_data = row.to_json(force_ascii=False)
                f.write(json_data)
                if index < len(df) - 1:
                    f.write(',\n') 
                
            f.write('\n]')  