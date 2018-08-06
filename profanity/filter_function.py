food_products = ["apple","pie","orange","tomato","potato","apricot","clementine"]

def filterFruits(products):
    fruits = ["mandarin","apple","lemon","orange","avocado","apricot","clementine"]

    if(products in fruits):
        return True
    else:
        return False

filteredFruits = filter(filterFruits,food_products)

print("The filterd Fruits are: ")
for fruit in filteredFruits:
    print (fruit)
