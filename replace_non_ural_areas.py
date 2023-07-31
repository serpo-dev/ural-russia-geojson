import json

ural_areas = ["Пермскаякрай", "Курганскаяобласть", "Свердловскаяобласть", "Тюменскаяобласть", "Челябинскаяобласть", "Ханты-МансийскийАОк", "Ямало-НенецкийАОк"]

EXTRACT_URAL_FILENAME = "input_1_save_ural.json"
EXTRACT_NON_URAL_FILENAME = "input_2_save_non_ural.json"
OUTPUT_FILENAME = "output.json"

# Extract Ural areas from the first file

with open(EXTRACT_URAL_FILENAME, "r", encoding="utf-8") as input_to_save_ural_file:
    to_save_ural_data = json.load(input_to_save_ural_file)

features=to_save_ural_data["features"]
ural_features = []
for feature in features:
    properties = feature["properties"]
    name=properties["NL_NAME_1"]
    if name in ural_areas:
        ural_features.append(feature)

#Extract Non-Ural areas from the second file

with open(EXTRACT_NON_URAL_FILENAME, "r", encoding="utf-8") as input_to_save_non_ural_file:
    to_save_non_ural_data = json.load(input_to_save_non_ural_file)

features=to_save_non_ural_data["features"]

non_ural_features = []
for feature in features:
    properties = feature["properties"]
    name=properties["NL_NAME_1"]
    if name not in ural_areas:
        ural_features.append(feature)

# Comnine Ural and Non-Ural data and save topython output file

with open(OUTPUT_FILENAME, "w", encoding="utf-8") as output_file:
    data = {
        "type":"FeatureCollection",
        "name":"gadm41_RUS_3",
        "crs":{
            "type":"name",
            "properties":{
                "name":"urn:ogc:def:crs:OGC:1.3:CRS84"
                }},
                "features": ural_features + non_ural_features
    }

    json.dump(data, output_file, ensure_ascii=False)