from behave import *
#----- GET
@given("I'm sending the GET requests and I expect 200 status code")
def get_response(context):
    status_code = context.method.get_api_response()
    assert status_code == True
@when("I've received good status code, I should check if content is proper and does not contain error message")
def get_content(context):
    content = context.method.get_api_all_content()
    assert  content == True
@then("I want to check single api element's status code with id {id}")
def get_single_response(context, id):
    status_code = context.method.get_api_single_response(id)
    assert status_code == True
@then("I want to check single api element's content if free from errors with the same id {id}")
def get_single_content(context, id):
    content = context.method.get_api_single_content(id)
    assert content == True

#----- POST
@given("I'm sending the POST requests using the {name} {type} {urls} and I expect 200 status code")
def post_response(context, name, type, urls):
    status_code = context.method.api_post_response(name,type,[urls])
    assert status_code == True
@then("I want to verify if the POST content with the given name has been created {name}")
def post_content(context, name):
    content = context.method.api_post_content(name)
    assert content == True

#----- DELETE
@given("I've deleted api element with {id} and I expect the status_code 204")
def delete_response(context, id):
    status_code = context.method.del_api_response(id)
    assert  status_code == True
@then("I make sure the {id} has been deleted. I should receive Index out of the scope error")
def delete_content(context, id):
    content = context.method.del_api_content(id)
    assert  content == True

#----- PATCH
@given("I want to to edit {id} and change {key} to {value}. I should get response 200")
def patch_response(context, id, key, value):
    response = context.method.api_patch_response(id, key, value)
    assert response == True

@then("I want to verify the {id} if the given change {key} to {value} has been saved")
def patch_content(context, id, key, value):
    content = context.method.api_patch_content(id, key, value)
    assert content == True

