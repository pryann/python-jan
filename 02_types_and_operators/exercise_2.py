# 2. Írj egy programot, amely kiszámolja egy derékszögű háromszög hiányzó oldalát Pitagorasz tételével!
# A felhasználó adja meg az ismert oldalakat, majd a program határozza meg a hiányzó oldalt és írja ki az eredményt!

import math

a = float(input("Kérem az első befogó hosszát:  "))
b = float(input("Kérem a második befogó hosszát:  "))

c = math.sqrt(a**2 + b**2)
print("A háromszög átfogója: ", c)
