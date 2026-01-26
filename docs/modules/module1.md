# Module 1: Fundamentals

This module covers the fundamental concepts of implied cost of capital.

## Learning Objectives

By the end of this module, you will be able to:

* Define test helo
* Understand the different models used
* Apply basic calculations

## Topics Covered

### Basic Models

The most common models for calculating implied cost of capital include:

#### 1. Dividend Discount Model (DDM)

The Gordon Growth Model is a simplified version:

$$r = \frac{D_1}{P_0} + g$$

Where:

* $r$ = required rate of return (cost of equity)
* $D_1$ = expected dividend next year
* $P_0$ = current stock price
* $g$ = constant growth rate

#### 2. Residual Income Model

(Add content here)

#### 3. Abnormal Earnings Growth Model

(Add content here)

## Practical Example

Let's walk through a simple example...

```python
def calculate_gordon_growth_icc(dividend, price, growth_rate):
    """
    Calculate ICC using Gordon Growth Model
    
    Args:
        dividend: Expected dividend next year (D1)
        price: Current stock price (P0)
        growth_rate: Constant growth rate (g)
    
    Returns:
        Required rate of return (r)
    """
    return (dividend / price) + growth_rate

# Example calculation
icc = calculate_gordon_growth_icc(2.0, 50.0, 0.05)
print(f"Implied Cost of Capital: {icc:.2%}")  # Output: 9.00%
```

## Key Takeaways

```{note}
The Gordon Growth Model is best suited for mature companies with stable dividend growth rates.
```

```{warning}
Always validate your assumptions about growth rates - they significantly impact the results!
```
