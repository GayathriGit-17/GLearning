def make_pizza(*toppings):
    for topping in toppings:
        print(topping)


Gayathri = make_pizza("tomato")
Ishant = make_pizza("mushroom,olives,onion")
Logha = make_pizza("cheese", "corn", "salsa")


def make_pizza2(*toppings, base):
    for topping in toppings:
        print(topping, base)


Gayathri = make_pizza2("tomato", base="thin")
Ishant = make_pizza2("mushroom,olives,onion", base="crust")
Logha = make_pizza2("cheese", "corn", "salsa", base="pan")

# Function scope global and local

global a=10


def my_local_var():
    a = 10
