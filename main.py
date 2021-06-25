import random

numbers = [1, -1, 2, -2, 3, -3]

k = random.randint(10, 26)
i = random.choice(numbers)

print(
    " " * k + " *" + "\n" + " " * (k - i) + " *" + "\n" + " " * k + " *" + "\n" + " " * (k + i) + " *" + "\n" + " " * (
                k + 2 * i) + " *" + "\n" + " " * (k + 3 * i) + " *" + "\n" + " " * (k + 2 * i) + " *" + "\n" + " " * (
                k + i) + " *" + "\n" + " " * k + " *")

decorations = ["*" * 15, "_" * 15, "+" * 15, "o" * 15, "-" * 15, "=" * 15, "^" * 15, ".:." * 5, "*.*" * 5,
               ":*::*::*::*::*:", "oOoooOoooOoooOo", "/*\/*\/*\/*\/*\ ", "^_^" * 5, "`" * 15, "~" * 15, "<^>" * 5,
               "o*_*o" * 3]

gifts = ["Dolphin", "Car", "Cat", "Dog", "Ticket to a Zoo", "Dragon Toy", "Bubble Making Toy", "Clock", "Book", "Bunny",
         "Candies", "Hug", "Glasses", "Video Game", "50 Bitcoins", "Jacket", "One sock", "Empty Cardboard Box",
         "Mobile Phone", "PC", "PS5", "Vitamins", "Underwear", "Kiss", "Balloons", "Miniature tree", "Diamond",
         "Mansion", "Tank", "Laser", "Lamp", "Yo-Yo", "Frisbee", "Fridge", "Shampoo", "Fruits", "Ball",
         "Spiderman costume", "Coconut soap", "Piano", "Flowers", "Bicycle", "Vacuum cleaner", "Board Game",
         "Smartwatch", "Huge Chocolate", "Black Wine", "Backpack", "Laptop", "Blanket", "Chinese Dictionary",
         "Personal Swimming Pool", "Boxing Gloves", "T-Shirt", "Sneakers", "Digital Camera", "Washing Machine",
         "Mini Car for Kids", "Headphones", "Cap", "Aquarium", "Free Paragliding", "Room with 1000 pillows",
         "Energy Drink", "Surfing Board", "Free Massage", "Jetpack", "Golden Neckless", "Train Toy", "+Self-Esteem ;)"]

received = random.sample(gifts, 3)
a = received[0]
b = received[1]
c = received[2]

x = random.choice(decorations)
# pick random decorator
y = " " * 10


# align


def decor(func):
    print(y, x)
    func()
    print(y, x)
    return decor


# def decorator

@decor
def text():
    print("           HAPPY BIRTHDAY!")


text

cake = """

  Here's your cake !


                   *
                   |
                   |
                ___|___
               |       |
              -----------
             |===========|
            ---------------
           |```````````````|
           ~~~~~~~~~~~~~~~~~


"""

print("""









            OPENING GIFTS...



                ...



        happiness intensifies...





        . . . 



                . . .






            you are smiling :D








                          . . .





                .   .   .





    happiness reaching critical level







            .   .   .

















                    . . .







            YOU RECEIVED :

           :D  {}

           :D  {}

           :D  {}

{}




   <<< Play again for more giftS >>>

""".format(a, b, c, cake))






























