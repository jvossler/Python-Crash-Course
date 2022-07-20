def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print(f"Making a {size}-inch pizza with the folling toppings:")
    for topping in toppings:
        print(f"- {topping}")