import scrapy
import pandas as pd

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
            yield response.follow(link, self.parse_pokemon, cb_kwargs={'pokemon_url': link})

    def parse_pokemon(self, response, pokemon_url):
        name = response.css('h1::text').get()
        number = response.css('th:contains("National Dex No") + td::text').get()
        weight = response.css('th:contains("Weight") + td::text').get()
        height = response.css('th:contains("Height") + td::text').get()
        types = response.css('table.vitals-table tr:contains("Type") a::text').getall()

        if number is not None:
            try:
                number = int(number.strip())
            except ValueError:
                number = None

        if weight is not None:
            try:
                weight = float(weight.strip())
            except ValueError:
                weight = None

        if height is not None:
            try:
                height = float(height.strip())
            except ValueError:
                height = None

        evolution_data = []
        evolution_rows = response.css('table.evochain-table tbody tr')
        for evolution_row in evolution_rows:
            poke_num = evolution_row.css('td:nth-child(2)::text').get()
            poke_name = evolution_row.css('td:nth-child(3) a::text').get()
            poke_link = evolution_row.css('td:nth-child(3) a::attr(href)').get()
            
            if poke_num is not None:
                try:
                    poke_num = int(poke_num.strip())
                except ValueError:
                    poke_num = None
                
            evolution_data.append({
                'PokeNum': poke_num.strip(),
                'Nome': poke_name.strip(),
                'URL': poke_link,
            })

        abilities_link = response.css('th:contains("Abilities") + td a::attr(href)').get()
        abilities_name = response.css('th:contains("Abilities") + td a::text').get()
        
        if abilities_link is None:
            abilities_link = "NONE"
        if abilities_name is None:
            abilities_name = "NONE"

        pokemon_data = {
            "Numero": number,
            "URL da pagina": pokemon_url,
            "Nome": name.strip() if name else "",
            "Tamanho": height,
            "Peso": weight,
            "Tipos": types,
            "Proximas evolucoes": evolution_data,
            "Habilidades": {
                "URL da pagina": abilities_link,
                "Nome": abilities_name,
            }
        }

        self.pokemons_data.append(pokemon_data)

    def closed(self, reason):
        df = pd.DataFrame(self.pokemons_data)
        df.to_json('pokedex.json', orient='records')