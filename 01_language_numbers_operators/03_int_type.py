# literál: egy olyan adat, amelyet közvetlenül a forráskódban írunk le
# a memória foglalás dinamikusan történik
# az int típusnak nincs felső vagy alsó határa a Pythonban (csak a rendelkezésre álló memória korlátozza)

print(1000)  # 1000
print(1e10)  # 10000000000.0
print(1e-4)  # 0.0000000001

# az int típusú literálokban használhatunk aláhúzásokat a jobb olvashatóság érdekében
print(12_123_098)  # 12123098
print(-1000)  # -1000
print(type(1000))  # <class 'int'>
