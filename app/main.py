class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = []

    for person in people:
        name, age = person["name"], person["age"]
        para = Person(name, age)
        person_list.append(para)

    for pars in people:
        person_obj = Person.people[pars["name"]]

        if "wife" in pars and pars["wife"] is not None:
            person_obj.wife = Person.people[pars["wife"]]

        if "husband" in pars and pars["husband"] is not None:
            person_obj.husband = Person.people[pars["husband"]]

    return person_list
