# Kérj be egy szöveget a felhasználótól, majd írassuk ki az utolsó karakterét!
user_input = input("Kérlek, adj meg egy szöveget: ")
user_input_len = len(user_input)
last_index = user_input_len - 1
print(user_input[last_index])

# pythonian way
# print(user_input[-1])
