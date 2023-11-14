people = [
    {'name':'David','House':'Lagos'},
    {'name':'Ojo','House':'Abuja'},
    {'name':'Oluwatoyosi','House':'Oyo'},


]

# def f(person):
#     return person['house']

people.sort(key=lambda person:person['name'])


print(people)