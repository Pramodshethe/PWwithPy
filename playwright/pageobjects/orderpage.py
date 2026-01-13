from .orderdetails import OrderDetailsPage

class OrderPage:
    def __init__(self, page):
        self.page = page

    def select_order(self, orderID):
        row = self.page.locator("tr").filter(has_text=orderID)
        row.get_by_role("button", name="View").click()
        order_details_page = OrderDetailsPage(self.page)
        return order_details_page