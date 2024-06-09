import requests

while True:
    pokemon = input("Which pokemon do you want to find? (enter quit to exit) :")
    pokemon = pokemon.lower()

    if(pokemon=="quit"):
        print("exit")
        break

    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon}"

    req = requests.get(url)

    if req.status_code ==200:
        data = req.json()
        print(f"Name : {data['name']}")
        print("Abilities :")
        for ability in data['abilities']:
            print(ability['ability']['name'])
    else:
        print("Pokemon not found")
    

