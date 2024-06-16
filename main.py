import data
from sandwich_maker import SandwichMaker
from cashier import Cashier


# Make an instance of other classes here
resources = data.resources
recipes = data.recipes
sandwich_maker_instance = SandwichMaker(resources)
cashier_instance = Cashier()




def main():
    ###  write the rest of the codes ###
    while True:
        sandwich_size = input("Enter sandwich size (small, medium, large, off): ")
        if sandwich_size.lower() == "off":
            print("Turning off the sandwich maker. Goodbye!")
            break

        if sandwich_size in recipes:
            order_ingredients = recipes[sandwich_size]["ingredients"]
            if sandwich_maker_instance.check_resources(order_ingredients):
                cost = recipes[sandwich_size]["cost"]
                print("Your order costs: $", cost)
                coins = cashier_instance.process_coins()
                if cashier_instance.transaction_result(coins, cost):
                    change = coins - cost
                    sandwich_maker_instance.make_sandwich(sandwich_size, order_ingredients)
                    print("Your sandwich is being made. Enjoy!")
                    if change > 0:
                        print(f"Here is your change: ${change:.2f}")
                else:
                    print("Insufficient payment. Please try again.")
            else:
                print("Ingredients are not available to make your order.")
        else:
            print("Invalid option. Please enter a valid sandwich size.")
if __name__=="__main__":
    main()
