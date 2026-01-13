# dynamic vs static typing: fordítási időben ismert-e a típus vagy futásidőben dől el
# static: type check futtatás előtt
# dinamikus: type check futásidőben

age = 10  # dinamikus típus
age = "10"
age = "tíz"

# explicit vs implicit typing
# explicit: a programozó határozza meg a típust
# implicit: a fordító vagy interpreter határozza meg a típust

age = 10  # implicit típusmegadás
age = int("10")  # explicit típusmegadás

# type annotation
age: int = 10  # csak dokumentációs célokra szolgál, nem végzi el a típusellenőrzést
