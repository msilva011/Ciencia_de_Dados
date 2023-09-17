# Construção dos Seletores

> Um seletor CSS é a primeira parte de uma regra CSS. É um padrão de elementos e outros termos que informam ao navegador quais elementos HTML devem ser selecionados para que os valores de propriedade CSS dentro da regra sejam aplicados a eles.

1. Seletor para Pokémons na Tabela Inicial:
   pokemons = response.css('table#pokedex tbody tr')
   Este selecetor, procura por todos os elementos tr (linhas) dentro da tabela com o ID "pokedex". Cada linha representa um Pokémon na tabela inicial.

2. Seletor para o Link do Pokémon:
   link = pokemon.css("td:nth-child(2) a::attr(href)").get()
   Aqui, está dentro do loop que percorre cada linha da tabela de Pokémons. Este seletor busca o link (`<a>`) contido na segunda célula (`<td>`) de cada linha. O atributo ::attr(href) é usado para extrair o valor do atributo "href" do elemento âncora (`<a>`).

3. Seletor para o Nome do Pokémon:
   name = response.css('h1::text').get()
   Este seletor procura pelo texto dentro do elemento h1 na página. O nome do Pokémon está contido dentro deste elemento.

4. Seletor para o Número do Pokémon:
   number = response.css('th:contains("National Dex No") + td::text').get()
   Este seletor procura pelo valor do número do Pokémon, que está dentro da célula da tabela localizada logo após a célula cujo cabeçalho contém o texto "National Dex No".

5. Seletor para o Peso do Pokémon:
   weight = response.css('th:contains("Weight") + td::text').get()
   Este seletor busca o valor do peso do Pokémon, que está dentro da célula da tabela localizada logo após a célula cujo cabeçalho contém o texto "Weight".

6. Seletor para a Altura do Pokémon:
   height = response.css('th:contains("Height") + td::text').get()
   Da mesma forma, este seletor busca o valor da altura do Pokémon, que está dentro da célula da tabela logo após a célula cujo cabeçalho contém o texto "Height".

7. Seletor para Tipos do Pokémon:
   types = response.css('table.vitals-table tr:contains("Type") a::text').getall()
   Este seletor procura por todos os elementos âncora (`<a>`) que estão dentro das células de uma tabela com a classe "vitals-table" e contêm o texto "Type". Isso permite extrair todos os tipos do Pokémon.

8. Seletor para Próximas Evoluções do Pokémon:
   evolution_rows = response.css('table.evochain-table tbody tr')
   Aqui, busca-se todas as linhas (tr) dentro da tabela com a classe "evochain-table". Isso nos ajuda a coletar informações sobre as próximas evoluções do Pokémon.

9. Seletor para Habilidades do Pokémon:
   abilities_link = response.css('th:contains("Abilities") + td a::attr(href)').get()
   abilities_name = response.css('th:contains("Abilities") + td a::text').get()
   Estes seletores procuram pelo link e pelo nome das habilidades do Pokémon. O primeiro seletor extrai o atributo "href" do elemento âncora, enquanto o segundo extrai o texto do elemento âncora.

### Exemplo resultado:

```
{"Numero":null,"URL da pagina":"\/pokedex\/squirtle","Nome":"Squirtle","Tamanho":null,"Peso":null,"Tipos":["Water"],"Proximas evolucoes":[],"Habilidades":{"URL da pagina":"\/ability\/torrent","Nome":"Torrent"}}
```