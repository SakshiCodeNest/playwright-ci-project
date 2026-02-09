import time
from pages.amazonfind_pages import amazon_productfind_pages

def test_search_phone(page):
    amz_find  = amazon_productfind_pages(page)
    amz_find.open_amazon_page()
    amz_find.search_product("POCO C71, Desert Gold (4GB, 64GB)")
    time.sleep(5)
    amz_find.click_first_product("C71, Desert Gold (4GB, 64GB)")
    time.sleep(10)

def test_search_laptop(page):
    amz_find  = amazon_productfind_pages(page)
    amz_find.open_amazon_page()
    amz_find.search_product("Dell 15 Laptop, 14th Gen Intel Core 3 100U Processor")
    time.sleep(5)
    amz_find.click_first_product("15 Laptop, 14th Gen Intel Core 3 100U Processor, 16GB DDR4, 512 SSD, Intel UHD Graphics, 15.6\" NT FHD 120Hz IPS AG 250 nit Display, Win 11 + Office H&S 2024, Carbon Black, Thin & Light- 1.63Kg")
    time.sleep(10)

def test_search_washingmachine(page):
    amz_find  = amazon_productfind_pages(page)
    amz_find.open_amazon_page()
    amz_find.search_product("Whirlpool 9 Kg 5 Star Fully Automatic Top Load Washing Machine (MAGIC CLEAN PRO BW H 9 KG Mn GREY 10YMW with In-Built Heater")
    time.sleep(5)
    amz_find.click_first_product("9 Kg 5 Star MAGIC CLEAN BW PRO Heater Fully Automatic Top Load Washing Machine (MAGIC CLEAN PRO BW H 9 KG Mn GREY 10YMW with In-Built Heater, 2025)")
    time.sleep(10)
    

def test_search_airconditioner(page):
    amz_find  = amazon_productfind_pages(page)
    amz_find.open_amazon_page()
    amz_find.search_product("ac 1.5 ton 5 star inverter split")
    time.sleep(5)
    amz_find.click_first_product("Lloyd 1.5 Ton 5 Star Inverter Split AC (5 in 1 Convertible, Anti Corrosion Coating, Copper, PM 2.5 Filter, White with Chrome Deco Strip, GLS18I5KWGGW)")
    time.sleep(10)
    