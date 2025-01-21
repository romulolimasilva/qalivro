from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By

@given('que estou na página de login')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.get("http://exemplo.com/login")

@when('eu preencho o campo "{field}" com "{value}"')
def step_impl(context, field, value):
    context.driver.find_element(By.NAME, field).send_keys(value)

@when('eu clico no botão "{button_text}"')
def step_impl(context, button_text):
    context.driver.find_element(By.XPATH, f"//button[text()='{button_text}']").click()

@then('eu devo ver a mensagem "{message}"')
def step_impl(context, message):
    assert message in context.driver.page_source
    context.driver.quit()
