bread = ["white bread", "black bread"]
meat = ["beef", "chicken"]
vegetables = ["tomatoes", "cucumbers"]
sauces = ["ketchup", "kmayonnaise"]

for b in bread:
    for m in meat:
        for v in vegetables:
            for s in sauces:  print("Sandwich:", b, m, v, s)
              