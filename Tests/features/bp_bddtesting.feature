Feature: Blood Pressure Calculator Title
  Scenario: Blood Pressure Calculator Systolic Value Input on Application
    Given launch chrome browser
    When open blood pressure calculator
    Then verify the container for systolic value input exists
    And close browser

  Scenario: Blood Pressure Calculator Diastolic Value Input on Application
    Given launch chrome browser
    When open blood pressure calculator
    Then verify the container for diastolic value input exists
    And close browser


  Scenario: Blood Pressure Calculator Diastolic Value Input on Application
      Given launch chrome browser
      When open blood pressure calculator
      Then verify the calculate blood pressure button exists
      And close browser