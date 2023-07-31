import json

with open("gadm41_RUS_1.json", "r", encoding="utf-8") as input_file:
    data = json.load(input_file)

features=data["features"]

NL_NAME_1_LIST = []

for feature in features:
    properties = feature["properties"]
    name=properties["NL_NAME_1"]
    if name not in NL_NAME_1_LIST:
        NL_NAME_1_LIST.append(name)

with open("NL_NAME_1_LIST-level-1.txt", "w", encoding="utf-8") as output_file:
    for i in NL_NAME_1_LIST:
        output_file.write(i + "\n")