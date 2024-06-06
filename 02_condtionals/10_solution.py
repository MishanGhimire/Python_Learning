## Problem: Recommend a type of pet food based on the pet's species and age. (e.g., Dog: <2 years - Puppy food, Cat: >5 years - Senior cat food).
species = "Dog"
age = 1  

if species == "Dog":
    if age < 2:
        pet_food = "Puppy food"
    elif 2 <= age <= 7:
        pet_food = "Adult dog food"
    else:
        pet_food = "Senior dog food"
elif species == "Cat":
    if age < 1:
        pet_food = "Kitten food"
    elif 1 <= age <= 5:
        pet_food = "Adult cat food"
    else:
        pet_food = "Senior cat food"
else:
    pet_food = "Unknown species"


print(f"Recommended food for a {age}-year-old {species}: {pet_food}")