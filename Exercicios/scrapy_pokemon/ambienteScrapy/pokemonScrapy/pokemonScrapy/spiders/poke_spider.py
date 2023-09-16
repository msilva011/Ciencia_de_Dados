import scrapy
import pandas as pd
import jsonlines

class PokeSpider(scrapy.Spider):
    name = 'pokespider'
    start_urls = ['https://pokemondb.net/pokedex/all']

    def __init__(self, *args, **kwargs):
        super(PokeSpider, self).__init__(*args, **kwargs)
        self.pokemons_data = []

    def parse(self, response):
        pokemons = response.css('table#pokedex tbody tr')
        for pokemon in pokemons:
            link = pokemon.css("td:nth-child(2) a::attr(href)").get()
            yield response.follow(link, self.parse_pokemon)

    def parse_pokemon(self, response):
        name = response.css('h1::text').get()
        number = response.css('th:contains("National Dex No") + td::text').get()
        weight = response.css('th:contains("Weight") + td::text').get()
        height = response.css('th:contains("Height") + td::text').get()
        types = response.css('table.vitals-table tr:contains("Type") a::text').getall()

        # Verifica se os campos são None e aplica strip() ou define como string vazia
        if number is not None:
            number = number.strip()
        else:
            number = ""

        if weight is not None:
            weight = weight.strip()
        else:
            weight = ""

        if height is not None:
            height = height.strip()
        else:
            height = ""

        pokemon_data = {
            "Nome": name.strip() if name else "",
            "Número": number,
            "Peso": weight,
            "Altura": height,
            "Tipos": types
        }

        self.pokemons_data.append(pokemon_data)  # Adiciona os dados à lista

        yield pokemon_data 

    def closed(self, reason):
        # Converte Scrapy x DataFrames
        df = pd.DataFrame(self.pokemons_data)

        # Arquivo CSV
        df.to_csv('pokemons.csv', index=False)

        # Arquivo Json
        with jsonlines.open('pokemons.json', mode='w') as writer:
            writer.write_all(self.pokemons_data)
