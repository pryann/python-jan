# a | b | a and b
# ---------------
# 0 | 0 |   0
# 0 | 1 |   0
# 1 | 0 |   0
# 1 | 1 |   1

age = 30

if age < 18:
    print("Kiskorú")
elif age >= 18 and age < 65:
    print("Felnőtt")
else:
    print("Nyugdíjas")

# a | b | a or b
# ---------------
# 0 | 0 |   0
# 0 | 1 |   1
# 1 | 0 |   1
# 1 | 1 |   1

prog_lang = "Python"

if prog_lang == "Python" or prog_lang == "JavaScript":
    print("Script nyelv")
else:
    print("Nem script nyelv")

# IN REAL LIFE
script_languages = ["Python", "JavaScript", "Ruby", "PHP", "Perl"]
if prog_lang in script_languages:
    print("Script nyelv")
else:
    print("Nem script nyelv")


temperature = 50
humidity = 60
rain = True

# in real app DO NOT USE magic values like this, use constants or config files
if temperature > 30 or humidity < 70 and not rain:
    print("Dry and hot weather v1")
# not rain                        ---->   False
# humidity < 70                   ---->   True
# humidity < 70 and not rain      ---->   True and False --> False
# temperature > 30                ---->   True
# temperature > 30 or False       ---->   True or False --> True


if (temperature > 30 or humidity < 70) and not rain:
    print("Dry and hot weather v2")
