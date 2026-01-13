from .orderpage import OrderPage

class Dashboard:
    def __init__(self, page):
        self.page = page

    def selectOrdersNavLink(self):
        self.page.get_by_role("button", name='ORDERS').click()
        order_page = OrderPage(self.page)
        return order_page
