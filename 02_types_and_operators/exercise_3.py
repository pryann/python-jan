# 3. Adott egy szöveges változó, amiben egy mondat található. Írj programot, ami az összes "_e_" karaktert "_a_"
#    karakterre cseréli a mondatban, ezt tárold el egy új változóban! Írd ki az új értéket!
#    A mondat a következő: "_Lorem ipsum dolor sit amet, consectetur adipiscing elit_"

sentence = "Lorem ipsum dolor sit amet, consectetur adipiscing elit"
new_sentence = sentence.replace("e", "a")
print(new_sentence)
