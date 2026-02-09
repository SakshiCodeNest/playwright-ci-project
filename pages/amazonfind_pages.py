from conftest import page


class amazon_productfind_pages:
    def __init__(self, page):
        self.page = page
        self.textbox_search = page.get_by_placeholder("Search for products, brands and more")

    # ---------- Common ----------

    def open_amazon_page(self):
        self.page.goto("https://www.amazon.in")
        self.page.reload()  ###########################

        # if self.page.get_by_role("button", name="Continue shopping").is_visible():
        #     self.page.click()
        # else:
        #     print("Popup not visible, proceeding with test")
            # pass
        # Click on Continue shopping
        # self.page.get_by_role("button", name="Continue shopping").click()

    # ---------- Search ----------
    def search_product(self, product_name):
        self.page.get_by_placeholder("Search Amazon.in").fill(product_name)
        self.page.keyboard.press("Enter")

    def click_first_product(self, product_name):
        with self.page.expect_popup() as page1_info:
            self.page.get_by_role("link", name=product_name,  exact=True).click()
        page1 = page1_info.value
        #Adding to cart
        page1.get_by_role("button", name="Add to cart").click()
        #Proceed to buy
        page1.get_by_role("button", name="Proceed to Buy (1 item) Buy").click()

    def test_mobile_menu(self, mobile_page):
        self.mobile_page = mobile_page
        self.mobile_page.goto("https://www.amazon.in")
        self.mobile_page.click("#nav-hamburger-menu")
        assert self.mobile_page.locator("text=Shop by Category").is_visible()