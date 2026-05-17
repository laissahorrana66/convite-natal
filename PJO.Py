# Percy Jackson Interactive RPG
# Feito em Python puro (terminal)
# Conversas infinitas, múltiplas rotas e escolhas

import random
import time

player_name = ""
relationship = {
    "Annabeth": 0,
    "Percy": 0,
    "Nico": 0,
    "Clarisse": 0,
    "Leo": 0
}

inventory = []
gold = 1000
energy = 100

locations = [
    "Acampamento Meio-Sangue",
    "Arena de Treino",
    "Floresta Encantada",
    "Praia de Poseidon",
    "Cabana 13",
    "Refeitório",
    "Lago dos Monstros"
]

def slow(text):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(0.02)
    print()

def menu():
    print("\n===== MENU =====")
    print("1 - Explorar")
    print("2 - Conversar")
    print("3 - Ver Status")
    print("4 - Inventário")
    print("5 - Missão Aleatória")
    print("6 - Dormir")
    print("0 - Sair")

def status():
    print("\n===== STATUS =====")
    print(f"Nome: {player_name}")
    print(f"Ouro: {gold}")
    print(f"Energia: {energy}")
    print("\nRelacionamentos:")
    for k, v in relationship.items():
        print(f"{k}: {v}")

def explore():
    global energy
    place = random.choice(locations)
    slow(f"\nVocê foi para: {place}")

    events = [
        "Você encontrou um item raro.",
        "Um monstro apareceu!",
        "Você viu alguém treinando.",
        "Achou dracmas perdidos.",
        "Encontrou uma passagem secreta."
    ]

    event = random.choice(events)
    slow(event)

    if "item" in event:
        item = random.choice([
            "Espada Celestial",
            "Poção Azul",
            "Escudo Grego",
            "Colar Místico"
        ])
        inventory.append(item)
        slow(f"Você ganhou: {item}")

    elif "dracmas" in event:
        gain = random.randint(50, 300)
        slow(f"Você ganhou {gain} dracmas!")

    elif "monstro" in event:
        battle()

    energy -= 5

def battle():
    global energy
    monsters = [
        "Minotauro",
        "Hidra",
        "Ciclope",
        "Empousa"
    ]

    monster = random.choice(monsters)
    slow(f"\n⚔️ Um {monster} apareceu!")

    while True:
        print("\n1 - Atacar")
        print("2 - Fugir")

        choice = input("> ")

        if choice == "1":
            if random.randint(1, 10) > 3:
                slow(f"Você derrotou o {monster}!")
                reward = random.randint(100, 400)
                slow(f"Ganhou {reward} dracmas.")
                break
            else:
                damage = random.randint(5, 20)
                energy -= damage
                slow(f"Você levou {damage} de dano.")
                if energy <= 0:
                    slow("Você desmaiou...")
                    energy = 50
                    break

        elif choice == "2":
            slow("Você fugiu!")
            break

def talk():
    global energy

    characters = list(relationship.keys())

    print("\nCom quem deseja falar?")
    for i, char in enumerate(characters):
        print(f"{i+1} - {char}")

    try:
        choice = int(input("> ")) - 1
        character = characters[choice]
    except:
        slow("Escolha inválida.")
        return

    conversations = {
        "Annabeth": [
            "Annabeth: Estratégia é mais importante que força.",
            "Annabeth: Você gosta de arquitetura grega?",
            "Annabeth: Talvez você seja útil em missões."
        ],
        "Percy": [
            "Percy: Já enfrentei monstros piores.",
            "Percy: Quer ir até a praia depois?",
            "Percy: Cuidado com os deuses."
        ],
        "Nico": [
            "Nico: Nem tudo é o que parece.",
            "Nico: O submundo é silencioso demais.",
            "Nico: Você confia em mim?"
        ],
        "Clarisse": [
            "Clarisse: Quero ver você sobreviver na arena.",
            "Clarisse: Não seja fraco.",
            "Clarisse: Talvez você tenha potencial."
        ],
        "Leo": [
            "Leo: Explosões acidentais acontecem.",
            "Leo: Quer ver minha invenção nova?",
            "Leo: Aposto que consigo melhorar sua espada."
        ]
    }

    slow("\n" + random.choice(conversations[character]))

    print("\n1 - Responder gentilmente")
    print("2 - Flertar")
    print("3 - Ser rude")

    response = input("> ")

    if response == "1":
        relationship[character] += 2
        slow(f"{character} gostou da conversa.")
    elif response == "2":
        relationship[character] += 5
        slow(f"{character} ficou corado(a).")
    elif response == "3":
        relationship[character] -= 3
        slow(f"{character} parece irritado(a).")

    energy -= 2

def inventory_menu():
    print("\n===== INVENTÁRIO =====")

    if not inventory:
        print("Vazio.")
    else:
        for item in inventory:
            print("-", item)

def mission():
    global gold
    global energy

    missions = [
        "Recuperar um artefato perdido.",
        "Derrotar monstros na floresta.",
        "Proteger um semideus novato.",
        "Explorar ruínas antigas.",
        "Encontrar uma relíquia dos deuses."
    ]

    mission_selected = random.choice(missions)

    slow(f"\nMISSÃO: {mission_selected}")

    print("\n1 - Aceitar")
    print("2 - Recusar")

    choice = input("> ")

    if choice == "1":
        if random.randint(1, 10) > 2:
            reward = random.randint(300, 1000)
            gold += reward
            relationship[random.choice(list(relationship.keys()))] += 3
            slow(f"Missão concluída! +{reward} dracmas.")
        else:
            damage = random.randint(10, 30)
            energy -= damage
            slow(f"A missão deu errado. -{damage} energia.")
    else:
        slow("Você recusou a missão.")

def sleep_player():
    global energy
    slow("\nVocê descansou.")
    energy = 100

# INTRO
slow("===== PERCY JACKSON RPG =====")
player_name = input("Digite seu nome: ")

slow(f"\nBem-vindo(a), {player_name}!")
slow("Você chegou ao Acampamento Meio-Sangue...")

# LOOP INFINITO
while True:

    if energy <= 0:
        slow("\nVocê está sem energia.")
        sleep_player()

    menu()

    option = input("> ")

    if option == "1":
        explore()

    elif option == "2":
        talk()

    elif option == "3":
        status()

    elif option == "4":
        inventory_menu()

    elif option == "5":
        mission()

    elif option == "6":
        sleep_player()

    elif option == "0":
        slow("\nSaindo do jogo...")
        break

    else:
        slow("Opção inválida.")
