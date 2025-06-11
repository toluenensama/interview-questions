import psycopg2
import random

data = "GREEN, YELLOW, GREEN, BROWN, BLUE, PINK, BLUE, YELLOW, ORANGE, CREAM, ORANGE, RED, WHITE, BLUE, WHITE, BLUE, BLUE, BLUE, GREEN, ARSH, BROWN, GREEN, BROWN, BLUE, BLUE, BLEW, PINK, PINK, ORANGE, ORANGE, RED, WHITE, BLUE, WHITE, WHITE, BLUE, BLUE, BLUE, GREEN, YELLOW, GREEN, BROWN, BLUE, PINK, RED, YELLOW, ORANGE, RED, ORANGE, RED, BLUE, BLUE, WHITE, BLUE, BLUE, WHITE, WHITE, BLUE, BLUE, GREEN, WHITE, BLUE, BROWN, PINK, YELLOW, ORANGE, CREAM, ORANGE, RED, WHITE, BLUE, WHITE, BLUE, BLUE, BLUE, GREEN, GREEN, WHITE, GREEN, BROWN, BLUE, BLUE, BLACK, WHITE, ORANGE, RED, RED, RED, WHITE, BLUE, WHITE, BLUE, BLUE, BLUE, WHITE"
data_list = data.split(", ")


day_num = len(data_list) // 5
week_data = [data_list[i * day_num:(i + 1)* day_num] for i in range(5)]

week_tally = {}

for color in data_list:
    week_tally[color] = week_tally.get(color,0) + 1



# Question one: The mean of a categorical data cannot be calculated


# Question two: 

highest_freq_color = max(week_tally,key=week_tally.get) # type: ignore
highest_freq = week_tally[highest_freq_color]
print("Most worn throughout the week:")
print(f"{highest_freq_color} : {highest_freq}")
print("\n")


# Question three:
sorted_list = sorted(data_list)
median_pos = int(len(sorted_list) / 2)
print("The color which is median is: ")
print(sorted_list[median_pos])
print("\n")


# Question five:
# Probabilty of selecting RED at random is given by the frequency of RED divided by the total amount of data entries
red_freq = week_tally["RED"]
probabilty_of_red = float((red_freq) / len(data_list))
print("Probability of picking a RED at random: ")
print(probabilty_of_red)
print("\n")


# Question six:

connection =  psycopg2.connect(
    dbname='colors',
    user='postgres',
    password='secret_password',
    host="localhost",
    port="5432"

)

cursor = connection.cursor()

cursor.execute("""
CREATE TABLE color_frequencies (
               id SERIAL PRIMARY KEY,
               color VARCHAR(10),
               freq INT)
""")

for key,val in week_tally.items():
    cursor.execute(
        """
INSERT INTO color_frequencies(color,freq) VALUES (%s,%s)
""",(key,val)
    )

connection.commit()
cursor.close()
connection.close()

# Question seven:
lst = [1,2,3,4,5,6,7,8,9,12,34,56,78,90]

def findVal(num,index=0):
    if lst[index] == num:
        return (f"Found {num} at {lst.index(num)}")
    if index >= len(lst):
        return ("not found")
    return findVal(num,index + 1)

print(findVal(5))
print("\n")

# Question eight:
def generate_rand():
    digits=""
    for _ in range(4):
        digits += str(random.randint(0,1))
    deci = int(digits,2)
    return f"Binary: {digits}, Decimal:{deci}"

print(generate_rand())
print("\n")

# Question nine:
n = 50
a,b = 0,1
sequence = []
for _ in range(n):
    sequence.append(a)
    a,b = b,a+b
print(f"Sum of the first 50 terms of the fibbonacci sequence: {sum(sequence)}")

