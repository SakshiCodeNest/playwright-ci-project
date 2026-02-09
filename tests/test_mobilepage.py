import time
from pages.amz_mobilepage import amazon_mobilepage_view as amz_mobilepage

def test_mobile_menu(mobile_page):
    amz_page = amz_mobilepage(mobile_page)
    amz_page.open_amazon_page()
    amz_page.test_mobile_menu()
    time.sleep(2)
    