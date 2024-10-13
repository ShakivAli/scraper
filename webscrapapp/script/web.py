import requests
from selenium import webdriver
from bs4 import BeautifulSoup
import time

# class ThreeListsDict:
#     def _init_(self):
#         self.elements = {}

#     def add_lists(self, keys, values1, values2):
#         for key, value1, value2 in zip(keys, values1, values2):
#             self.elements[key] = (value1, value2)

#     def print_items_with_colons(self):
#         for key, values in self.elements.items():
#             print(f"{key}:{values[1]}:{values[0]}")

#     def get_values1(self, key):
#         if key in self.elements:
#             return self.elements[key][0]
#         else:
#             return None
        
# res_link = []
# res_name = []
# res_rate = []
# url = "https://www.swiggy.com/city/jalandhar/best-restaurants"
# header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

# r = requests.get(url, headers=header)

# soup = BeautifulSoup(r.text, 'html.parser')

# p = soup.find_all(class_='RestaurantList__RestaurantAnchor-sc-1d3nl43-3 kcEtBq')
# q = soup.find_all(class_='sc-beySbM lfjhyG')
# r = soup.find_all(class_='sc-beySbM fA-DJGp')

# for i in p:
#     res_link.append(i.get('href'))

# for i in q:
#     res_name.append(i.string)

# for i in r:
#     res_rate.append(i.text)

# restaurant_dict = ThreeListsDict()
# restaurant_dict.add_lists(res_name, res_link, res_rate)

# # restaurant_dict.print_items_with_colons()
# print(restaurant_dict.get_values1("Pizza Hut"))

# #taking input of restaurant and hit the url
# restaurant_dict_input = input()
# restaurant_dict_input_link = restaurant_dict.get_values1(restaurant_dict_input)
# print(restaurant_dict.get_values1(restaurant_dict_input))

# hit_res_link = requests.get(restaurant_dict_input_link,'html.parser')


# #using the selenium for the menu of each restaurant
# driver = webdriver.Chrome()
# driver.get(restaurant_dict_input_link)

# # Wait for dynamic content to load (you may need to adjust the wait time)
# time.sleep(2)  # Example wait time

# # Get the page source
# page_source = driver.page_source

# # Close the webdriver
# driver.quit()

# # Parse the page source with Beautiful Soup
# soup_res_link = BeautifulSoup(page_source, 'html.parser')

# # Now you can use Beautiful Soup to find elements as usual
# # For example, find all elements with a specific class
# elements = soup_res_link.find_all(class_="styles_itemNameText__3ZmZZ")
# price = soup_res_link.find_all(class_="rupee")

# res_menu = []
# menu_price = []
# res_menu_price = dict(zip(res_menu, menu_price))

# # Process the elements as needed
# for element in elements:
#     res_menu.append(element.text)

# for p in price:
#     menu_price.append(p.text)    

# res_menu_price = dict(zip(res_menu, menu_price))

# var = "Crispy Veg Double Patty Burger+Fries(M)"
# for m, p in res_menu_price.items():
#     if(m == var): print(f"{m}  :  {p}")







# res_menu = []
# menu_price = []
# res_menu_price = dict(zip(res_menu, menu_price))
# def get_menu_list(restaurant_dict_input_link):
#     #using the selenium for the menu of each restaurant
#     driver = webdriver.Chrome()
#     driver.get(restaurant_dict_input_link)

#     # Wait for dynamic content to load (you may need to adjust the wait time)
#     time.sleep(2)  # Example wait time

#     # Get the page source
#     page_source = driver.page_source

#     # Close the webdriver
#     driver.quit()

#     # Parse the page source with Beautiful Soup
#     soup_res_link = BeautifulSoup(page_source, 'html.parser')

#     # Now you can use Beautiful Soup to find elements as usual
#     # For example, find all elements with a specific class
#     elements = soup_res_link.find_all(class_="styles_itemNameText__3ZmZZ")
#     price = soup_res_link.find_all(class_="rupee")

#     for element in elements:
#         res_menu.append(element.text)

#     for p in price:
#         menu_price.append(p.text) 

 
# #taking input of restaurant and hit the url
# restaurant_dict_input = input()
# restaurant_dict_input_link = restaurant_dict.get_values1(restaurant_dict_input)
# print(restaurant_dict.get_values1(restaurant_dict_input))

# hit_res_link = requests.get(restaurant_dict_input_link,'html.parser')
# get_menu_list(restaurant_dict_input_link)

# # Process the elements as needed
# res_menu_price = dict(zip(res_menu, menu_price))

# var = "Crispy Veg Double Patty Burger+Fries(M)"
# for m, p in res_menu_price.items():
#     print(f"{m}  :  {p}")




import requests
from selenium import webdriver
from bs4 import BeautifulSoup
import time

url = "https://www.coingecko.com/en/highlights/trending-crypto"
header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

r = requests.get(url, headers=header)

#list of names of trending bitcoins and links
bit_name = []
bit_links = []
bit_name_link = dict(zip(bit_name, bit_links))

#using the selenium for the menu of each restaurant
driver = webdriver.Chrome()
driver.get(url)

# Wait for dynamic content to load (you may need to adjust the wait time)
time.sleep(2)  # Example wait time

# Get the page source
page_source = driver.page_source

# Close the webdriver
driver.quit()

# Parse the page source with Beautiful Soup
soup = BeautifulSoup(page_source, 'html.parser')

# Now you can use Beautiful Soup to find elements as usual
# For example, find all elements with a specific class
elements = soup.find_all(class_="tw-text-gray-700 dark:tw-text-moon-100 tw-font-semibold tw-text-sm tw-leading-5")
links = soup.find_all(class_="tw-flex tw-items-center tw-w-full")

c=0
for i in elements:
    bit_name.append(i.text)
    c+=1                                      
    if c==10: break

c=0
for i in links:
    bit_links.append(i.get("href"))
    c+=1
    if c==10: break

for i in bit_links:
    print(i,"\n")