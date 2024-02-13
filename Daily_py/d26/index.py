info = "My name is {} and Im from {}"
name = "Biologist"
country = "Pakistan"
print(info)
print(info.format(name, country))
info = "My name is {} and Im from {}"
print(info.format(country, name))
# can change the position by using indexes in {}
info = "My name is {1} and Im from {0}"
print(info.format(country, name))
# but ya diffecut ha thora agar 10k ho to bari bari index dekhna pry ga...so use f string

# in f string we can directly put variables in it
info = f"My name is {name} and Im from {country}"
print(info)

# another example by using string formate
txt = "For only {price:.2f} dollars"
print(txt.format(price=44.667))

# another example by using f string
price = 2.444
txt = f"For only {price:.2f} dollars"
print(txt)

# another example by using f string
print(f"{50+50}")
print(type(f"{50+50}"))

# if you wanna print curly brackets insted of value so put double curly brackets
info = f"My name is {{name}} and Im from {{country}}"
print(info)
