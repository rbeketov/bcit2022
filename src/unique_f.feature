Feature: test Unique
    
    Scenario: Test my class Unique (any)
        Given the list F, f
        When Unique them
        Then result to be f

    Scenario: Test my class Unique none
        Given the list None
        When Unique them
        Then result to be None

    Scenario: Test my class Unique digit
        Given the list 3, 3, 6
        When Unique them
        Then result to be 3, 6