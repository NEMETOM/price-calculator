Feature: Price calculations

    Scenario: Apply discount correctly
        Given the original price is 100
        When I apply a discount of 10 percent
        Then the final price should be 90
        
    Scenario: Add VAT correctly
        Given the original price is 100
        When I add VAT of 20 percent
        Then the final price should be 120
