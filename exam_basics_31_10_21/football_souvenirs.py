team = input()
souvenir = input()
quantity = int(input())

price = 0
teams = ["Argentina", "Brazil", "Croatia", "Denmark"]
souvenirs = ["flags", "caps", "posters", "stickers"]

if team not in teams:
    print("Invalid country!")

elif souvenir not in souvenirs:
    print("Invalid stock!")

else:
    if team == "Argentina":
        if souvenir == "flags":
            price = 3.25
        elif souvenir == "caps":
            price = 7.20
        elif souvenir == "posters":
            price = 5.10
        elif souvenir == "stickers":
            price = 1.25

    elif team == "Brazil":
        if souvenir == "flags":
            price = 4.20
        elif souvenir == "caps":
            price = 8.50
        elif souvenir == "posters":
            price = 5.35
        elif souvenir == "stickers":
            price = 1.20

    elif team == "Croatia":
        if souvenir == "flags":
            price = 2.75
        elif souvenir == "caps":
            price = 6.90
        elif souvenir == "posters":
            price = 4.95
        elif souvenir == "stickers":
            price = 1.10

    elif team == "Denmark":
        if souvenir == "flags":
            price = 3.10
        elif souvenir == "caps":
            price = 6.50
        elif souvenir == "posters":
            price = 4.80
        elif souvenir == "stickers":
            price = 0.90

    total_price = quantity * price

    print(f"Pepi bought {quantity} {souvenir} of {team} for {total_price:.2f} lv.")