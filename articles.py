import api_data
import pandas as pd

def get_statistics():
	url_statistics = 'https://seller-analytics-api.wildberries.ru/api/v2/nm-report/detail'

	# later read from file this data
	print("Enter data in format YYYY-MM-DD hh:mm:ss YYYY-MM-DD hh:mm:ss")
	# 2023-09-01 00:00:00 2024-04-11 23:59:59
	date = input().split()
	params = {"period": {
				"begin": date[0] + " " + date[1],
				"end": date[2] + " " + date[3]},
				"page": 1}

	request = api_data.get_data(url_statistics, params)
	DataFrame = pd.json_normalize(request['data']['cards'])
	params['page'] = 2
	while request['data']['isNextPage'] == True:
		request = api_data.get_data(url_statistics, params)
		data = pd.json_normalize(request['data']['cards'])
		DataFrame = pd.concat([DataFrame, data], ignore_index = True)
		params['page'] += 1

	

# DataFrame.to_excel('cards_statistics.xlsx')