# with open("weather_data.csv") as weather_data:
#     weather_data = weather_data.readlines()
#
#     for i in weather_data:
#         print(i)

# import csv
#
# with open("weather_data.csv") as weather_data:
#     data = csv.reader(weather_data)
#     temperatures = []
#     for row in data:
#         # temperatures = row[1]
#         if row[1] != "Temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# print(type(data))
# print(data["Temp"])

# data_dict = data.to_dict()
#
# temp = data["Temp"].to_list()
#
# max_temp = data.Temp.max()
fur_color = data["Primary_Fur_Color"].to_list()
gray_count = "Gray"
cin_count = 'Cinnamon'
black_count = "Black"

gray_count = data["Primary_Fur_Color"].value_counts()[gray_count]
cin_count = data["Primary_Fur_Color"].value_counts()[cin_count]
black_count = data["Primary_Fur_Color"].value_counts()[black_count]
# print(gray_count)

# print(fur_color)

sqrl_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_count, cin_count, black_count]

}
new_data = pandas.DataFrame(sqrl_dict)
print(new_data)
new_data.to_csv(".Squirrel_Count")

# Getting data in columns

# print(data.Condition)

# Get data in Row

# print(data[data.Day == "Monday"])
# print(data[data.Temp == max_temp])

# Tuesday = data[data.Day == "Tuesday"]
# temp = int(data.Temp)
#
# fahrenheit = (temp * 9/5) + 32
# print(f"{fahrenheit}")

# Creating a DataFrame from scratch

# data_dict = {
#     "students": ["Amy", "Elon", "Peter", "Steven", "Andrew"],
#     "scores": [20, 45, 60, 73, 55]
# }
#

# nw_data = pandas.DataFrame(data_dict)
# print(nw_data)
# nw_data.to_csv(".new_data.csv")
#
# print(nw_data.scores.max())
