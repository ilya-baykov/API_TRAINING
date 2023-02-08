import requests
import re

with open("dataset_24476_3.txt", "r") as data, open("answer.txt", "w") as answer:
    numbers = [int(i) for i in data]
    data.close()
    for number in numbers:
        param = {
            "json": "true"
        }
        res = requests.get(f"http://numbersapi.com/{number}/math", param)
        # res = requests.get(f"http://numbersapi.com/{number}", params=param)
        print(res.text)
        lst = re.findall(r"\"found\": false,", res.text)
        print(lst)
        print("-" * 50)
        if lst:
            answer.write("Boring\n")
        else:
            answer.write("Interesting\n")

    answer.close()
