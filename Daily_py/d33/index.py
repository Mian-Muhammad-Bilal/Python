info = {
    "biologist": "Alien", "Place": "Mars"
}
# print(info["biologist"])  # if not exists it throws error
# print(info.get("biologist"))  # if not exists it will give none
# print(info)  # print whole dictionary

# # for key in dick.keys():
# # print(dick[key])

# for key in info.keys():
#     print(f"The value correspnding to the key {key} is:{info[key]}")

print(info.items())
