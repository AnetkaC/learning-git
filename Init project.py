print("Lista zakupów".center(50, '='))
print()

shopping_list = ["chleb", "bułki", "pączek", "marchew", "seler", "rukola"]

shopping = {
    "piekarnia": ["chleb", "bułki", "pączek"],
    "warzywniak": ["marchew", "seler", "rukola"]
}

lenght = len(shopping_list)
for k, v in shopping.items():
    
    print("Idę do " + k.capitalize() + " i kupuję tam :" + str(v) + " ")
