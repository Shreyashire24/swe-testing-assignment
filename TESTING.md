# Testing Strategy

## What Was Tested

All four arithmetic operations were tested: addition, subtraction, multiplication, and division. The clear function was also tested. Edge cases include division by zero, negative numbers, decimal inputs, and very large numbers.

## What Was Not Tested

Performance, security, and scalability were not tested as they do not apply to a simple calculator.

## Overall Approach

Unit tests target individual functions in isolation. Integration tests verify that sequences of operations work correctly together.

## Lecture Concepts

### Testing Pyramid
Most tests (9 out of 11) are unit tests which are fast and isolated. Only 2 are integration tests. This matches the pyramid which says have many unit tests and fewer integration tests.

### Black-box vs White-box Testing
Unit tests used white-box testing because we know the internal logic and tested specific code paths like the division by zero check. Integration tests used black-box testing by treating the input and output as a system.

### Functional vs Non-Functional Testing
All tests are functional tests. They check that the calculator does what it is supposed to do. Non-functional testing was left out as it is out of scope.

### Regression Testing
Any future change to the calculator can be checked by running pytest tests/ to confirm everything still passes.

## Test Results

| Test Name | Type | Status |
|---|---|---|
| test_add_positive | Unit | PASS |
| test_subtract_positive | Unit | PASS |
| test_multiply_positive | Unit | PASS |
| test_divide_positive | Unit | PASS |
| test_divide_by_zero | Unit | PASS |
| test_add_negative_numbers | Unit | PASS |
| test_multiply_decimal | Unit | PASS |
| test_large_numbers | Unit | PASS |
| test_clear | Unit | PASS |
| test_full_calculation_sequence | Integration | PASS |
| test_clear_after_calculation | Integration | PASS |