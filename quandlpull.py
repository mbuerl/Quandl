import quandl


quandl.ApiConfig.api_key = 'jhkghJ59ybRRaM1E7QeK'
stock = quandl.get('FSE/WDI_X', column_index='1')
print(stock)