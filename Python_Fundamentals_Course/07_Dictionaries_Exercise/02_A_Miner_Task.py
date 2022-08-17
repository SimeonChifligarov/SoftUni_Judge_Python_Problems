# You will be given a sequence of strings, each on a new line.
# Every odd line on the console is representing a resource
# (e.g. Gold, Silver, Copper, and so on) and every even - quantity.
# Your task is to collect the resources and print them each on a new line.

resource = input()
resources_dict = {}

while not resource == "stop":
    quantity = int(input())
    if resource not in resources_dict:
        resources_dict[resource] = 0
    resources_dict[resource] += quantity
    resource = input()

for res, quant in resources_dict.items():
    print(f"{res} -> {quant}")
