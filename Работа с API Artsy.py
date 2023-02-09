import requests
import json

name = "Ilya"
Client_Id = "524556004070f9a6b07d"
Client_Secret = "1b4f1af1f4a2b78d8d0b8a828f3bea47"

# инициируем запрос на получение токена
r = requests.post("https://api.artsy.net/api/tokens/xapp_token",
                  data={
                      "client_id": Client_Id,
                      "client_secret": Client_Secret
                  })

# разбираем ответ сервера
j = json.loads(r.text)

# достаем токен
token = j["token"]

# создаем заголовок, содержащий наш токен
headers = {"X-Xapp-Token": token}

with open("dataset_24476_4.txt", "r") as data:
    DATA = {i.strip("\n"): "" for i in data}
    data.close()

for identifier in DATA:
    # инициируем запрос с заголовком
    r = requests.get(f"https://api.artsy.net/api/artists/{identifier}", headers=headers)

    # разбираем ответ сервера
    j = json.loads(r.text)
    DATA[identifier] = [int(j["birthday"]), j["sortable_name"]]

print(DATA)
print("-" * 20)
with open("answer_2.txt", "w") as answer_2:
    for artist in sorted(DATA.items(), key=lambda para: (para[1][0], para[1][1])):
        print(artist[1])
        answer_2.write(str((artist[1][1]).encode("utf-8")).strip("b'") + '\n')
    answer_2.close()
