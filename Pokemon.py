import random

# Define os Pokémon e seus atributos
pokemons = {
    "Squirtle": {"Level": 15, "HP": 150, "Ataque": 50, "Defesa": 65, "Tipo": "Water",
                 "Golpes": {"Water Gun": {"Power": 40, "Type": "Water"}, "Tackle": {"Power": 40, "Type": "Normal"},
                            "Water Pulse": {"Power": 50, "Type": "Water"}, "Bite": {"Power": 50, "Type": "Dark"}}},
    "Pikachu": {"Level": 15, "HP": 120, "Ataque": 55, "Defesa": 40, "Tipo": "Electric",
                "Golpes": {"Thunder Shock": {"Power": 40, "Type": "Electric"}, "Quick Attack": {"Power": 40, "Type": "Normal"},
                           "Electro Ball": {"Power": 50, "Type": "Electric"}, "Spark": {"Power": 55, "Type": "Electric"}}},
    "Charmander": {"Level": 15, "HP": 130, "Ataque": 52, "Defesa": 43, "Tipo": "Fire",
                   "Golpes": {"Ember": {"Power": 40, "Type": "Fire"}, "Scratch": {"Power": 40, "Type": "Normal"},
                              "Flamethrower": {"Power": 70, "Type": "Fire"}, "Dragon Breath": {"Power": 50, "Type": "Dragon"}}},
    "Bulbasaur": {"Level": 15, "HP": 140, "Ataque": 49, "Defesa": 49, "Tipo": "Grass",
                  "Golpes": {"Tackle": {"Power": 40, "Type": "Normal"}, "Vine Whip": {"Power": 45, "Type": "Grass"},
                             "Razor Leaf": {"Power": 55, "Type": "Grass"}, "Seed Bomb": {"Power": 80, "Type": "Grass"}}}
}

# Tabela de eficácia de tipos
eficaciaDano = {"Water": {"Fire": 2.0, "Water": 0.5, "Electric": 1.0, "Grass": 0.5},
                "Electric": {"Water": 2.0, "Electric": 0.5, "Fire": 1.0, "Grass": 0.5},
                "Fire": {"Water": 0.5, "Fire": 0.5, "Electric": 1.0, "Grass": 2.0},
                "Grass": {"Water": 2.0, "Electric": 1.0, "Fire": 0.5, "Grass": 0.5},
                "Normal": {"Water": 1.0, "Electric": 1.0, "Fire": 1.0, "Grass": 1.0},
                "Dark": {"Water": 1.0, "Electric": 1.0, "Fire": 1.0, "Grass": 1.0},
                "Dragon": {"Water": 1.0, "Electric": 1.0, "Fire": 1.0, "Grass": 1.0}}

def calculoDano(atacante, defensor, golpe):
    return int(golpe["Power"] * (atacante["Ataque"] / defensor["Defesa"]) * eficaciaDano[golpe["Type"]].get(defensor["Tipo"], 1.0))

def escolhaPokemon():
    escolhas = list(pokemons.keys())
    print("Escolha seu Pokémon:")
    for i, p in enumerate(escolhas, 1):
        print(f"{i}. {p}")
    while True:
        try:
            escolha = int(input("Digite o número da sua escolha: ")) - 1
            if escolha in range(len(escolhas)):
                return escolhas[escolha]
        except ValueError:
            pass
        print("Escolha inválida. Tente novamente.")

def escolhaGolpe(pokemon):
    golpes = list(pokemons[pokemon]["Golpes"].keys())
    print(f"Escolha um ataque para {pokemon}:")
    for i, golpe in enumerate(golpes, 1):
        print(f"{i}. {golpe}")
    while True:
        try:
            escolha = int(input("Digite o número da sua escolha: ")) - 1
            if escolha in range(len(golpes)):
                return golpes[escolha]
        except ValueError:
            pass
        print("Escolha inválida. Tente novamente.")

# Inicializa a batalha
pokemonJogador = escolhaPokemon()
pokemonOponente = random.choice([p for p in pokemons.keys() if p != pokemonJogador])
pokemonX, pokemonY = pokemons[pokemonJogador], pokemons[pokemonOponente]

print(f"\nVocê escolheu {pokemonJogador}!")
print(f"Seu oponente escolheu {pokemonOponente}!\n")

# Loop da batalha
while pokemonX["HP"] > 0 and pokemonY["HP"] > 0:
    golpeX = escolhaGolpe(pokemonJogador)
    golpeY = random.choice(list(pokemonY["Golpes"].keys()))

    print(f"\n{pokemonJogador} usou {golpeX}!")
    dano = calculoDano(pokemonX, pokemonY, pokemonX["Golpes"][golpeX])
    pokemonY["HP"] -= dano
    print(f"Causou {dano} de dano!")
    
    if pokemonY["HP"] <= 0:
        print(f"{pokemonOponente} desmaiou! Você venceu!")
        break

    print(f"{pokemonOponente} usou {golpeY}!")
    dano = calculoDano(pokemonY, pokemonX, pokemonY["Golpes"][golpeY])
    pokemonX["HP"] -= dano
    print(f"Causou {dano} de dano!")
    
    if pokemonX["HP"] <= 0:
        print(f"{pokemonJogador} desmaiou! Você perdeu!")
        break

    print(f"{pokemonJogador} HP: {pokemonX['HP']}")
    print(f"{pokemonOponente} HP: {pokemonY['HP']}\n")

print("Fim do Jogo")