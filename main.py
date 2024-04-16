import pandas as pd
import articles
import investors_data

def count(x, y):
	return y / x * 100

investors = investors_data.get_investors()
wb_statisticks = articles.combine_arts()
# investors = pd.read_excel('timur_first_con_no_dup.xlsx', index_col = None)
# wb_statisticks = pd.read_excel('cards_statistics_grouped.xlsx', index_col = None)
# print(investors.columns, wb_statisticks.columns)
DataFrame = investors.merge(wb_statisticks, on = 'Article', how = 'left')
DataFrame.to_excel('merged_inv_wb.xlsx')
DataFrame = DataFrame[['Gender', 'DescriptionText', 'TAS', 'Выкупы']]
DataFrame = DataFrame.groupby(['DescriptionText', 'Gender'], as_index = False).sum()
DataFrame['Процент выкупа'] = DataFrame.apply(lambda x: count(x.TAS, x.Выкупы), axis = 1)
DataFrame = DataFrame.rename(columns = {'TAS' : 'Закупка'})
DataFrame.to_excel('categories.xlsx')
