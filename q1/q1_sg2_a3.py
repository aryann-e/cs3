baseline_year = 1900

zodiac_animals = [
    ("Rat", "鼠 / Shǔ"), ("Ox", "牛 / Niú"), ("Tiger", "虎 / Hǔ"),
    ("Rabbit", "兔 / Tù"), ("Dragon", "龙 / Lóng"), ("Snake", "蛇 / Shé"),
    ("Horse", "马 / Mǎ"), ("Goat", "羊 / Yáng"), ("Monkey", "猴 / Hóu"),
    ("Rooster", "鸡 / Jī"), ("Dog", "狗 / Gǒu"), ("Pig", "猪 / Zhū")
]

birth_year = int(input("Enter your birth year: "))

if birth_year < baseline_year:
  print("Invalid Year, it should not be earlier than 1900")
else:
  year = (birthyear - baseline_year)%12
  eng_name, chi_name = zodiac_animals[year]
  print(f"\nYour Chinese Zodiac is : {eng_name} ({chi_name})")
