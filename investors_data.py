import pandas as pd

def crop_description(str):
	elem = str.split('-', 1)[0]
	if elem == 'T':
		return 'T-shirt'	
	return elem

def add_zero(str):
	if len(str) == 9:
		str = '0' + str
	return str

def crop_article(str):
	return str[1::]

def get_investors():
	timur = pd.read_excel('src/timur.xlsx')
	timur = timur[['Gender', 'DescriptionText', 'Article', 'TAS']]
	columns = timur['DescriptionText'].apply(crop_description)
	timur['DescriptionText'] = columns
	columns = timur['Article'].map(str).apply(crop_article)
	timur['Article']  = columns
	timur.to_excel('test_timur.xlsx')

	first_lot = pd.read_excel('src/1_лот.xlsx')
	first_lot = first_lot[['Gender', 'DescriptionText', 'АРТИКУЛЦВЕТ на сайте', 'PiecesQuantity']]
	first_lot = first_lot.rename(columns = {'АРТИКУЛЦВЕТ на сайте' : 'Article', 'PiecesQuantity' : 'TAS'})
	columns = first_lot['DescriptionText'].apply(crop_description)
	first_lot['DescriptionText'] = columns
	columns = first_lot['Article'].map(str).apply(add_zero)
	first_lot['Article'] = columns
	first_lot.to_excel('test_first.xlsx')

	connected = pd.concat([first_lot, timur])
	connected.to_excel('timur_first_con.xlsx')
	connected = connected.groupby(['Gender', 'DescriptionText', 'Article'], as_index = False).sum()
	connected.to_excel('timur_first_con_no_dup.xlsx')

get_investors()