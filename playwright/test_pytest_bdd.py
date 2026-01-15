import pytest
from pytest_bdd import given, when, then, parsers, scenarios

from pageobjects.login import LoginPage
from utils.apiBase import APIUtils

scenarios("features/ordertransaction.feature")  #features_base_dir=

@pytest.fixture
def shared_data():
    return {}

@given(parsers.parse("place the item order with {username} and {password}"))
def place_item_order(playwright, username, password, shared_data):
    user_credentials = {"userEmail": username, "userPassword": password}
    apiutils = APIUtils()
    order_id = apiutils.createorder(playwright, user_credentials)
    shared_data['order_id'] = order_id

@given('user is on landing page')
def user_on_landing_page(browser_instance, shared_data):
    login_page = LoginPage(browser_instance)
    login_page.navigate()
    shared_data['login_page'] = login_page

@when(parsers.parse('I login with {username} and {password}'))
def login_with_username_password(username, password, shared_data):
    login_page = shared_data['login_page']
    dashboard_page = login_page.login(username, password)
    shared_data['dashboard_page'] = dashboard_page

@when("navigate to orders page")
def navigate_to_order_page(shared_data):
    dashboard_page = shared_data['dashboard_page']
    order_page = dashboard_page.select_orders_nav_link()
    shared_data['order_page'] = order_page

@when("select the orderID")
def select_order_id(shared_data):
    order_page = shared_data['order_page']
    order_id = shared_data['order_id']
    order_detail = order_page.select_order(order_id)
    shared_data['order_detail'] = order_detail

@then("verify the order message is successfully displayed")
def verify_message(shared_data):
    order_detail = shared_data['order_detail']
    order_detail.verify_order_message()