from __future__ import annotations


class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    people_list = []
    wife_husband_dict = {}
    for item in people:
        name = item["name"]
        age = item["age"]
        wife = item.get("wife")
        husband = item.get("husband")
        person = Person(name, age)
        if "wife" in item.keys():
            if wife:
                person.wife = wife
            wife_husband_dict[name] = ["wife", wife]
        if "husband" in item.keys():
            if husband:
                person.husband = husband
            wife_husband_dict[name] = ["husband", husband]
        people_list.append(person)
    for key, value in wife_husband_dict.items():
        if value[0] == "wife" and value[1]:
            Person.people[key].wife = Person.people[value[1]]
        if value[0] == "husband" and value[1]:
            Person.people[key].husband = Person.people[value[1]]
    return people_list


people = [
    {"name": "Ross", "age": 30, "wife": "Rachel"},
    {"name": "Joey", "age": 29, "wife": None},
    {"name": "Rachel", "age": 28, "husband": "Ross"}
]
person_list = create_person_list(people)
# print(person_list[0].wife)
# print(person_list[1].wife)
# print(person_list[2].name)
# print(Person.people)
# print(hasattr(Person, "people"))
# print(len(Person.people))
# print(Person.people["Joey"].age)


# print(isinstance(person_list[0], Person)) # True
# print(person_list[0].name) == "Ross"
# print(person_list[0].wife is person_list[2]) # True
# print(person_list[0].wife.name) == "Rachel"
#
# print(person_list[1].name) == "Joey"
# print(person_list[1].wife)
# # AttributeError
#
# print(isinstance(person_list[2], Person)) # True
# print(person_list[2].name) == "Rachel"
# print(person_list[2].husband is person_list[0]) # True
# # The same as person_list[0]
# print(person_list[2].husband.name) == "Ross"
# person_list[2].husband.wife is person_list[2]  # True
#
# Person.people == {
#     "Ross": <__main__.Person object at 0x10c20ca60>,
#     "Joey": <__main__.Person object at 0x10c180a00>,
#     "Rachel": <__main__.Person object at 0x10c1804f0>
# }
