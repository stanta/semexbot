
def finbot1d (Stock_index, date1):
	from yahoo_finance import Share
	from pprint import pprint
	import json
	stock = Share(Stock_index)
	hist = (stock.get_historical(date1 , date1))
	pprint (hist)
	#r_dict = json.load(hist)
	#r_dict = json.loads(rstr.text)
	#pprint (r_dict)
	#r_arr=r_dict.get('response').get('docs') 
	if (hist <> ""):
		day = {hist[0].get('Open'), hist[0].get('Close')}
		return day 

def finbot_hist (Stock_index, date1, date2):
	from yahoo_finance import Share
	from pprint import pprint
	import json
	stock = Share(Stock_index)
	hist = (stock.get_historical(date1 , date2))
	#pprint (hist)
	#r_dict = json.load(hist)
	#r_dict = json.loads(rstr.text)
	#pprint (r_dict)
	#r_arr=r_dict.get('response').get('docs') 
	
	for day in hist:
		pprint ({day.get('Date'),day.get('Open'), day.get('Close'), (float(day.get('Open')) - float(day.get('Close'))) })
	return 
	
	
date1='2015-04-08'
date2='2015-05-08'
firm = 'INTC'
i=finbot_hist(firm,date1,date2)
#print i