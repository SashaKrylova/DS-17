# dateRates = [['10-2022', 10],
#              ['10-2022', 20],
#              ['09-2022', 30],
#              ['09-2022', 40],
#               ]
#
# # print(dateRates)
#
# monthRates = {}
#
# iterationMonth = ''
#
# for month, rate in dateRates:
#     if month == iterationMonth:
#         rateList.append(rate)
#         print(f'This is rateList{rateList}')
#         monthRates[month] = rateList
#         # monthRates[month] = monthRates[month] + rate
#     else:
#         rateList = []
#         monthRates[month] = rateList
#         rateList.append(rate)
#
#     iterationMonth = month
#
# print(monthRates)
from collections import defaultdict

date_rates = [['10-2022', 20],
              ['10-2022', 20],
              ['10-2022', 20],
              ['09-2022', 30],
              ['09-2022', 40]]

rates_by_month = defaultdict(list)

for month, rate in date_rates:
    rates_by_month[month].append(rate)

averages_by_month = []
for month, rates in rates_by_month.items():
    average_rate = sum(rates) / len(rates)
    month_dict = {'month': month, 'avg_rate': average_rate}
    averages_by_month.append(month_dict)

print(averages_by_month)
