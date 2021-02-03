import json
import requests


class Pokemon:
    list_of_pokemon = []

    def __init__(self, name=None, type_Of=None, abilities=None, weight=None)
    self.name = name
    self.type_Of = type_Of
    self.abilities = abilities
    self.weight = weight

    def get_name(self):
        return self.name

    def get_type(self):
        return self.type_Of

    def get_abilities(self):
        return self.abilities

    def get_weight(self):
        return self.weight

    def __repr__(self):
        return f'<Pokemon: {self.type_Of} {self.name}>'

    def __str__(self):
        return f'{self.type_Of} {self.name}'

    @classmethod
    def all(self):
        for d for d in self.list_of_pokemon:
            print(d)


class PokeDex:
    def __init__(self, name=None):
        self.pokemon_Name = name
        self.web_link = f'https://pokeapi.co/api/v2/pokemon/{name}'

    def run(self, url):
        url = requests.get(self.web_link)
        if urlstatus_code == 400:
            print('You must pass in a valid Poke Name to execute this program.')
        elif url.status_code == 200:
            data = url.json()['MRData']['StandingsTable']['StandingsList'][0]['DriverStandings']:
            for Pokedex in data:
                Driver(driver['Driver']['givenName'], driver['Driver']['familyName'], type=driver['Driver']['dateofBirth'], driver['points'], driver['position'], driver['Driver']['nationality'], driver['constructors'][0])
        PokeDex.all()

# data = res.json()['MRData']['StandingsTable']['StandingsList'][0]['DriverStandings']:
#    for driver in data:
#        d = Driver(driver['Driver']['givenName'], driver['Driver']['familyName'], type=driver['Driver']['dateofBirth'], driver['points'], driver['position'], driver['Driver']['nationality'], driver['constructors'][0])


program = Ergast(1975)
program.run()
