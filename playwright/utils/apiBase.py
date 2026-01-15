from playwright.sync_api import Playwright

orders_payload = {"orders": [{"country": "India", "productOrderedId": "6960eac0c941646b7a8b3e68"}]}


class APIUtils:

    def getToken(self, playwright: Playwright, user_credentials):
        user_email = user_credentials['userEmail']
        user_password = user_credentials['userPassword']
        request_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        response = request_context.post("api/ecom/auth/login",
                                        data= {"userEmail": user_email,
                                        "userPassword": user_password})
        assert response.ok
        print(response.json())
        response_body = response.json()
        return response_body["token"]

    def createorder(self, playwright: Playwright, user_credentials):
        token = self.getToken(playwright, user_credentials)
        api_req_con = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        response = api_req_con.post("/api/ecom/order/create-order",
                                    data=orders_payload,
                                    headers={"Authorization": token,
                                             "content-Type": "application/json"
                                             })
        print(response.json())
        response_body = response.json()
        orderid = response_body["orders"][0]
        return orderid
