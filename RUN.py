Enter the Actual path of DataBase
gold_market.db

#1. NULL : NoneType Means “know nothing about it”
#2. INTEGER : int Integers
#3. REAL : float 8-byte floating-point numbers
#4. TEXT : str Strings of characters
#5. BLOB : bytes Binary data

SQL>#Below command will fetch all tuples from CSV to SQL Table
SQL>grab('GOLD_WORLD.csv','GOLD')
SQL>
SQL>#A sample SQL query over stored table
SQL>select USD_AM,GBP_AM,EUR_AM from GOLD where USD_AM > 1840
 1843.0|1164.098|1354.948|
 1879.5|1177.115|1359.395|
 1844.0|1153.437|1311.989|
 1891.0|1172.859|1330.753|
 1896.5|1174.667|1341.136|
 1854.0|1143.809|1301.235|
 1850.0|1119.584|1279.303|
 1886.5|1138.641|1301.753|
1877.75| 1139.55|1303.179|
 1862.0|1126.914|1299.281|
SQL>
SQL>#Another query to put entire data into buffer for plotting
SQL>#This will use select1 instead of select, so don't expect output on console
SQL>select1 * from GOLD
SQL>
SQL>#A simple line plot
SQL>#Plotting just USD_AM of history
SQL>plot(1,1,True,'red',False,False,True,'yellow')
SQL>show()
SQL>
SQL>#A line plot containing 3 lines, each for USD,GBP,EUR
SQL>plot(1,1,True,'black')
SQL>plot(3,3,True,'blue')
SQL>plot(5,5,True,'green')
SQL>show()
SQL>
SQL>#A Scatter plot between USD_AM & USD_PM to show the connection between them
SQL>sctr(1,2)
SQL>show()
SQL>
SQL>#A Histogram to show the frequency of Rates in history of gold price in USD
SQL>hist(1,50,'red')
SQL>show()
