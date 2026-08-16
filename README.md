# CoinReference

### Additional Information I Would Usually Acquire Before Starting Work


- **What is the problem we are trying to solve?**

- **Why does this problem need to be solved?** *(I might be looking for non-technical solutions)*

- **Who is the user, and what is their ideal result for this tool?**

- **How will this application be accessed?**
    - One-time report?
    - Integrated into POS software?
- **Owner of the application / maintenance?**


## Goal

Print values from 1–100 using a minimum amount of coins for each value.

## Requirements

- Iterate from 1–100 cents, printing each value in its numeric form and coin-face representation
- Utilize functional programming

## Specifications

- **Input:** Positive integers from 1–100
- **Output:** Well-formatted string, creating a tabular view
- Note: Separate functionality that creates the string from functionality that calculates the coins

## Pseudocode

```
Coin type definition (description)

calculate_change(amount)
    guard clause for no remainder
        return
    use modulo operation to calculate remainder (divmod?)
    recurse until guard is true?

format_table(amount)
    call calculate_change for each value
    format output
        return
```

## Testing / Validation

- **Unit testing** for `calculate_change`, `format_table`
- **Integration testing** for `format_table` 

## Properties 
- The sum of the returned coins equals the value provided
- The minimum number of coins is returned