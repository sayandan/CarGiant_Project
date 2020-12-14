car_list = [['Honda', 'Civic', '4 Dr Hatch, Auto, Petrol, White, 2016 (16), 46,018 miles', 'Not Listed', 'SOLD TODAY'],
            ['Ford', 'Ford', '5 Dr Hatch, Manual, Petrol, Black, 2017 (66), 33,307 miles', 'Listed', 'SOLD TODAY'],
            ['Ford', 'Focus', '5 Dr Hatch, Manual, Petrol, Grey, 2016 (66), 34,075 miles', 'Listed', 'NOT SOLD'],
            ['Audi', 'Q2', 'SUV, Manual, Petrol, White, 2017 (67), 23,240 miles', 'Listed', 'NOT SOLD'],
            ['BMW', 'All 7-series', 'Saloon, Auto, Diesel,Grey, 2016 (66), 20,834 miles', 'Listed', 'NOT SOLD']]
#
# for i in range(len(car_list)):
#     if car_list[i][3] == 'Not Listed':
#         car_list[i].append('Not Added To Watchlist')
#     elif car_list[i][4] == 'SOLD TODAY':
#         car_list[i].append('Not Added To Watchlist')
#     else:
#         car_list[i].append('Added To Watchlist')
#
# for i in range(len(car_list)):
#     print(car_list[i])

#print([row[2] for row in car_list])

for i in range(len(car_list)):
    if car_list[i][3] == 'Listed':
        if car_list[i][4] == 'NOT SOLD':
            print(car_list[i])
            #print([row[2] for row in car_list])


# Dict ={}
# car_list = [
#             ['Honda', 'Civic', '4 Dr Hatch, Auto, Petrol, White, 2016 (16), 46,018 miles', 'Not Listed', 'SOLD TODAY'],
#            ['Ford', 'Focus', '5 Dr Hatch, Manual, Petrol, Black, 2017 (66), 33,307 miles', 'Not Listed', 'SOLD TODAY'],
#            ['Ford', 'Focus', '5 Dr Hatch, Manual, Petrol, Grey, 2016 (66), 34,075 miles', 'Listed', 'NOT SOLD'],
#            ['Audi', 'Q2', 'SUV, Manual, Petrol, White, 2017 (67), 23,240 miles', 'Listed', 'NOT SOLD'],
#            ['BMW', 'All 7-series', 'Saloon, Auto, Diesel, Grey, 2016 (66), 20,834 miles', 'Listed', 'NOT SOLD']]
# print(len(car_list))
#
# for i in range(len(car_list)):
#     Dict["Make"] = car_list[i][0]
#     Dict["Model"] = car_list[i][1]
#     Dict["Detail"] = car_list[i][2]
#     Dict["Is_Listed"] = car_list[i][3]
#     Dict["Is_Sold"] = car_list[i][4]
# print(Dict)

