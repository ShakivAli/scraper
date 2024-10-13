from django.shortcuts import render, HttpResponse
import requests
from selenium import webdriver
from bs4 import BeautifulSoup
import time

# url which is needed to get the restaurant lists and header for the url
url = "https://www.swiggy.com/city/jalandhar/best-restaurants"
header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

r = requests.get(url, headers=header)
soup = BeautifulSoup(r.text, 'html.parser')

# Create your views here.

def home(request):
    return render(request, 'home.html')

def foodpage(request):
    # list of restaurants available to user location
    rest_list = []
    q = soup.find_all(class_='sc-beySbM iKLEMo')
    for i in q:
        rest_list.append(i.string)
    return render(request, 'food.html', {'rest_list':rest_list})

def restsubmission(request):
    # getting all the values selected from the checkbox of available restaurants
    submitted_rest_names = request.POST.getlist('options')

    # storing the selected resturants in the list
    list_of_selected_rest = submitted_rest_names

    # have to find all the restaurants available
    rest_name = []
    q = soup.find_all(class_='sc-beySbM iKLEMo')
    for i in q:
        rest_name.append(i.string)
    
    # to get the rating of a all the restaurant
    res_ratings = []
    r = soup.find_all(class_='sc-beySbM brneVe')
    for i in r:
        res_ratings.append(i.text)

    # pairing up the restaurants names with its ratings 
    paired_res_name_and_rating = dict(zip(rest_name,res_ratings))

    # get only selected rest names's ratings
    selected_rest_ratings = []
    for selected_rest in list_of_selected_rest:
        if selected_rest in paired_res_name_and_rating:
            rating = paired_res_name_and_rating[selected_rest]
            selected_rest_ratings.append(rating)

    # zipped selected rest names with their ratings
    zipped_selected_rest_and_ratings = zip(list_of_selected_rest,selected_rest_ratings)


    res_link = []
    # appending all the links of all the restaurants in the list
    l = soup.find_all(class_='RestaurantList__RestaurantAnchor-sc-1d3nl43-3 kcEtBq')    
    for i in l:
        res_link.append(i.get('href'))

    # pairing up the res name with their links
    res_name_link = dict(zip(rest_name,res_link))    

    # menu list of selected restaurants using a function passing list of selected elements one by one
    list_of_menus = [[]]

    # function as described above
    def get_menu_list(rest):
        #using the selenium for the menu of each restaurant
        driver = webdriver.Chrome()
        driver.get(rest)

        # Wait for dynamic content to load (you may need to adjust the wait time)
        time.sleep(2)  # Example wait time

        # Get the page source
        page_source = driver.page_source

        # Close the webdriver
        driver.quit()

        # Parse the page source with Beautiful Soup
        soup_res_link = BeautifulSoup(page_source, 'html.parser')

        # Now you can use Beautiful Soup to find elements as usual
        # For example, find all elements with a specific class
        elements = soup_res_link.find_all(class_="sc-aXZVg cjJTeQ sc-hIUJlX gCYyvX")
        price = soup_res_link.find_all(class_="sc-eZkCL erfDC")
        menu_list = []
        for element in elements:
            menu_list.append(element.text)

        
        c=0
        n=len(menu_list)
        for p in price:
            menu_list[c] = f"{menu_list[c]} &nbsp; &nbsp; <span class='price'>[Rs. {p.text}]</span>"
            c+=1
            if c==n:
                break
       
        return menu_list

    # one by one sending the rest names whom menu we want
    for rest in list_of_selected_rest:
        list_of_menus.append(get_menu_list(res_name_link[rest]))
    
    # context of multiple data
    context = {
        'list_of_menus': list_of_menus, 
        'zipped_selected_rest_and_ratings' : zipped_selected_rest_and_ratings,
    }

    return render(request, 'foodresult.html', context) 





url2 = "https://www.coingecko.com/en/highlights/trending-crypto"
# header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

r2 = requests.get(url2, headers=header)


def blockchainpage(request):
    blockchain_list = []
    driver2 = webdriver.Chrome()
    driver2.get(url2)
    time.sleep(2)
    page_source = driver2.page_source
    driver2.quit()
    soup2 = BeautifulSoup(page_source, 'html.parser')
    blockchains_names = soup2.find_all(class_="tw-text-gray-700 dark:tw-text-moon-100 tw-font-semibold tw-text-sm tw-leading-5")
    c = 0
    for i in blockchains_names:
        blockchain_list.append(i.text)
        c+=1
        if c==10:
            break

    return render(request, 'blockchain.html',{'blockchain_list':blockchain_list})

def blockchainsubmission(request):
     # getting all the values selected from the checkbox of available blockchains
    submitted_block_names = request.POST.getlist('options')

    # storing the selected blockchains in the list
    list_of_selected_block = submitted_block_names

    # for getting all the info inside the blockchain
    def get_info(selected_blockchain):
        
        return

    final_list = []
    for i in list_of_selected_block:
        final_list.append(get_info(i))

    context = {

    }

    return render(request, 'blockchainresult.html',{'context':context})