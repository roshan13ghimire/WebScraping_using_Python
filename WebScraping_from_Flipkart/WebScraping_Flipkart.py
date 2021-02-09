from bs4 import BeautifulSoup as bsoup              
from urllib.request import urlopen as uReq


my_url = 'https://www.flipkart.com/search?q=laptop&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off' #url of the search
uClient = uReq(my_url)
html_page = uClient.read()
uClient.close()
page_soup = bsoup(html_page,"html.parser")


containers = page_soup.findAll("div" , {"class" : "_3O0U0u"})   


fname = "Laptop.csv"  
f = open(fname,"w")                          #opening a file and write our searched items in that file
headers = "Prod_Name,Price,Ratings\n"
f.write(headers)
for container in containers:                    #using loop to traverse all the searched items in the first page
    try:
        product_name = container.div.img["alt"]    #accessing the product name


        Price_Container = container.findAll("div" ,{"class" : "col col-5-12 _2o7WAb"})   #accessing the price of the product
        Price = Price_Container[0].text.strip()                                           #splitting the price so that we can access only price instead of accessing discount amount and etc
 

        Ratings_Container = container.findAll("div" , {"class" : "niH0FQ"})               #accessing the rating of the product
        Ratings = Ratings_Container[0].text                                               #splitting the rating so that we can access only rating instead of accessing all other things.


        trim_price = ''.join(Price.split(','))        
        rm_rupee = trim_price.split("₹")       
        add_rs_price = "RS." + rm_rupee[1]           #replacing ₹ as RS.


        split_price = add_rs_price.split("E")
        final_price = split_price[0]


        split_rating = Ratings.split(",")
        final_rating = split_rating[0]


        print(product_name.replace("," , " |") + "," + final_price + "," + final_rating + "\n")      #printing all the elements
        f.write(product_name.replace("," , " |") + "," + final_price + "," + final_rating + "\n")    #writing all the elements in the file
    except IndexError:
        break
f.close()

