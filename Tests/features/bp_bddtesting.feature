Feature: Blood Pressure Calculator Title
  Scenario: Blood Pressure Calculator Title on Application
    Given launch chrome browser
    When open blood pressure calculator
    Then verify the container for systolic value input exists
    And close browser