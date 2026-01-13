# 5. Írj egy programot, amely bekéri a felhasználó nevét és korát, majd kiírja az adatait egy mondatban!
#    pl.: _A felhasználó neve Gipsz Jakab, és 33 éves._

name = input("Kérem adja meg a nevét: ")
age = input("Kérem adja meg az életkorát: ")

user = f"A felhasználó neve {name}, és {age} éves."
print(user)
