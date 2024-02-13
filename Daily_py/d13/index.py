a = "!!!Biologist !!!"
print(len(a))
print(a)
print(a.upper())
print(a.lower())
print(a.strip("!"))
print(a.rstrip("!"))  # strip the triling given char not leading
print(a.replace("Biologist", "Bilal"))
print(a.split(" "))
print(a.count("!"))
print(a.endswith("!"))
print(a.startswith("!"))
print(a.endswith("!", 4, 10))  # 4 sy 10 tk ! ha ya ni
print(a.find("o"))  # mil jay to us ka index(first occurence) dy ga ni to -1

# mil jay to us ka index(first occurence) dy ga ni to error ay ga
print(a.index("!"))
print(a.isalnum())  # atoz 1to0
print(a.isalpha())  # atoz
print(a.islower())
print(a.isupper())
print(a.isprintable())
print(a.isspace())
print(a.istitle())
print(a.swapcase())  # cap to lowercase and lowercase to upper case
print(a.title())  # first letter of the each word im to upper


heading = "intro to pythOn course"
print(heading.capitalize())  # first char to upper and all other to lower

canter = "wellcome!!!"
print(len(canter))
print(len(canter.center(22)))
print(canter.center(22))
