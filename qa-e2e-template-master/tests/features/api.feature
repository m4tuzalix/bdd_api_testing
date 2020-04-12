Feature: Test API

  @api_GET
  Scenario Outline: API_GET_TESTS
    Given I'm sending the GET requests and I expect 200 status code
    When I've received good status code, I should check if content is proper and does not contain error message
    Then I want to check single api element's status code with id <id>
    And I want to check single api element's content if free from errors with the same id <id>

    Examples: GET_data
      |id|
      |e74847d1-adb7-4213-905b-6811dca90b42|

  @api_POST
  Scenario Outline: API_POST_TESTS
    Given I'm sending the POST requests using the <name> <type> <urls> and I expect 200 status code
    Then I want to verify if the POST content with the given name has been created <name>

    Examples: POST_data
      |name|type|urls|
      |123zxc|web|https://examples.ru|

   @api_DELETE
  Scenario Outline: API_DELETE_TESTS
    Given I've deleted api element with <id> and I expect the status_code 204
    Then I make sure the <id> has been deleted. I should receive Index out of the scope error

    Examples: DELETE_data
      |id|
      |1234|

  @api_PATCH
  Scenario Outline: API_PATCH_TESTS
    Given I want to to edit <id> and change <key> to <value>. I should get response 200
    Then I want to verify the <id> if the given change <key> to <value> has been saved
    Examples: PATCH_data
      |id|key|value|
      |e74847d1-adb7-4213-905b-6811dca90b42|name|La Wroclavia|