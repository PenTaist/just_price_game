from random import randint

just_price = randint(1, 1000)

running = True

while running:
	user_price = int(input("Entrez un prix"))

	if user_price == just_price:
		print("Trouvé !")
		running = False

	elif user_price < just_price:
		print("C'est plus")

	elif user_price > just_price:
		print("C'est moins")


rejouer = input("Voulez vous rejouer ? (oui, non)")

if rejouer == "oui":
	running = True
else:
	running = False
