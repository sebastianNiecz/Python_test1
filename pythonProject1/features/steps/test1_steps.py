from behave import *
from Pages.PageBase import PageBase

page_base = PageBase()
button_locator = "//div[@class='FPdoLc lJ9FBc']//input[@name='btnK']"
input_locator = "//textarea[@id='APjFqb']"

@given(u'I am a user on the specified "{page}" page')
def i_am_a_user_on_the_specified_page(context, page):
    page_base.go_to_specified_page(page)

@when(u'I should see search button')
def should_see_search_button():
    assert page_base.find_specified_element(button_locator) == True

@when(u'I should see name of the button {locator_name}')
def i_should_see_name_of_the_button(locator_name):
    page_base.get_text(button_locator)
    assert button_locator == locator_name

@when(u'I set name {company_name} in search element input')
def i_set_name_in_search_element_input(company_name):
    page_base.input_name(company_name, input_locator)

@when(u'I click search button')
def i_click_search_button():
     page_base.click(button_locator)

@then(u'I should see found page name {page_name}')
def i_should_see_found_page_name(page_name):
        searched_page = "$//*[text()[contains(.,'{page_name}')]]"
        var = PageBase.find_specified_element(searched_page)
        return var is True