from playwright.sync_api import Playwright

orderspayload = {"orders": [{"country": "India", "productOrderedId": "6960eac0c941646b7a8b3e68"}]}


class APIUtils:

    def getToken(self, playwright: Playwright):
        request_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        response = request_context.post("api/ecom/auth/login",
                                        data= {"userEmail": "PWTest@gmail.com",
                                        "userPassword": "PWTestPWTest1"})
        assert response.ok
        print(response.json())
        responseBody = response.json()
        return responseBody["token"]

    def createorder(self, playwright: Playwright):
        token = self.getToken(playwright)
        api_req_con = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        response = api_req_con.post("/api/ecom/order/create-order",
                                    data=orderspayload,
                                    headers={"Authorization": token,
                                             "content - type": "application / json"
                                             })
        print(response.json())
