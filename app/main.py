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
