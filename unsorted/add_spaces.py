import json

# СОЗДАНИЕ ФАЙЛА ДЛЯ РЕДАКТИРОВАНИЯ НАЗВАНИЙ

# NAMES = []
# with open("output_ural_level_4.json", "r", encoding="utf-8") as r_file:
#     data = json.load(r_file)
#     for d in data["features"]:
#         name = {
#             "ru": d["properties"]["NL_NAME_2"].replace("район", " район").replace("(горсовет)", "").replace("(город)", ""),
#             "en": d["properties"]["NAME_2"].replace("rayon", " district").replace("gorsovet", "").replace("gorod", ""),
#         }
#         NAMES.append(name)
# with open("output_ural_level_4_names.json", "w", encoding="utf-8") as w_names_file:
#     json.dump(NAMES, w_file, ensure_ascii=False)



# =====================================================================
# ЧТЕНИЕ ФАЙЛА С РЕДАКТИРОВАННЫМИ  НАЗВАНИЯМИ И ЗАПИСЬ ИХ В ПОЛНЫЙ JSON

with open("output_ural_level_4_names.json", "r", encoding="utf-8") as r_names_file:
    names = json.load(r_names_file)
with open("output_ural_level_4.json", "r", encoding="utf-8") as r_file:
    data = json.load(r_file)

with open("output_ural_level_4_with_spaces.json", "w", encoding="utf-8") as w_with_spaces_file:
    for (i, d) in enumerate(data["features"]):
        d["properties"]["NL_NAME_2"] = names[i]["ru"]
        d["properties"]["NAME_2"] = names[i]["en"]
    json.dump(data, w_with_spaces_file, ensure_ascii=False)