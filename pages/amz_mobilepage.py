from conftest import mobile_page


class amazon_mobilepage_view:
    def __init__(self, mobile_page):
        self.page = mobile_page
        self.textbox_search = mobile_page.get_by_placeholder("Search for products, brands and more")

    def open_amazon_page(self):
        self.page.goto("https://www.amazon.in")
        self.page.reload()

    def test_mobile_menu(self):
        self.page.goto("https://www.amazon.in")
        self.page.click("#nav-hamburger-menu")
        mob_button = self.page.get_by_role("link", name="Mobiles").is_visible() 
        print(f"Is 'Mobiles' link visible? {mob_button}")
        self.page.get_by_role("link", name="Mobiles").click()  
        print("Mobile menu clicked successfully")

       
