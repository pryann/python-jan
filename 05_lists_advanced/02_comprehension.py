net_prices = [1000, 13450, 22000]
tax_rate = 0.27
# gross_prices = []

# for net_price in net_prices:
#     gross_price = net_price * (1 + tax_rate)
#     gross_prices.append(gross_price)

gross_prices = [i * (1 + tax_rate) for i in net_prices]

print(gross_prices)

values = [
    1,
    2,
    3,
    5,
    4,
    1,
    0,
    6,
    7,
    4,
    3,
]

# comprehension to filter out grades between 1 and 5
grades = [i for i in values if 0 < i < 6]
print(grades)

generated_list = [i for i in range(10)]
print(generated_list)

matrix = [[j for j in range(3)] for i in range(3)]
print(matrix)

rpg_games = [
    ["Earthdown", "Call of Cthulhu", "D&D"],
    ["Rifts", "M.A.G.U.S", "Blades in the dark"],
    ["Cyberpunk", "Shadowrun", "Star Wars"],
]

flatten_rpg_games = [game for sublist in rpg_games for game in sublist]
print(flatten_rpg_games)
