pupils_by_house = {
    'Slytherin': [],
    'Hufflepuff': [],
    'Gryffindor': [],
    'Ravenclaw': []
}

number = int(input())
for i in range(number):
    name = input()
    house = input()
    pupils_by_house[house].append(name)

for house in pupils_by_house:
    print(house + ':')
    for pupil in pupils_by_house[house]:
        print(pupil)
    print()
