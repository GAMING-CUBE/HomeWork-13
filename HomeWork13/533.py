program_lang_devs = {
    "James Gosling" : "Java",
    "Dennis Ritchie" : "C",
    "Guido Rossum" : "Python"
}

inpt = input()

for dev, lang in program_lang_devs.items():
    dev_split = dev.split()
    if inpt == dev_split[0] or inpt == dev_split[1]:
        print(lang)