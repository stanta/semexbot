
def finbot (Stock_index, date1, date2):
	from yahoo_finance import Share
	from pprint import pprint
	import json
	stock = Share(Stock_index)
	pprint (stock)
	#print stock.get_open(date1)
	#print stock.get_close(date1)
	#print stock.get_price(date1)
	#print stock.get_trade_datetime()
	r_dict = json.loads((stock.get_historical(date1 , date1)))
	#r_dict = json.loads(rstr.text)
	pprint (r_dict)
	#r_arr=r_dict.get('response').get('docs') 
	return 
	
	
date1='2015-04-01'
date2='2015-04-01'
firm = 'INTC'
i=finbot(firm,date1,date2)
