from inherit import Cat, Dog


def animal_sound(animals):
    for animal in animals:
        print(animal.name, end=" ")
        if isinstance(animal, Dog):
            print(animal.bark())
        elif isinstance(animal, Cat):
            print(animal.meow())


dogs = [Dog("spiky", "german shepard"), Dog("buddy", "golden retriever")]
cats = [Cat("whiskers", "persian"), Cat("lucy", "siamese")]

animals = dogs + cats
animal_sound(animals)
