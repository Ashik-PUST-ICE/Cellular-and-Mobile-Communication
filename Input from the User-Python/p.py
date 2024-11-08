import math

def erlang_b_formula(C, A):
    """Calculate the Erlang B blocking probability."""
    numerator = (A ** C) / math.factorial(C)
    denominator = sum((A ** k) / math.factorial(k) for k in range(C + 1))
    return numerator / denominator

def find_traffic_intensity(C, target_PB, tolerance=1e-4):
    """Find the traffic intensity A for a given C and target blocking probability."""
    A = 0.0
    step = 0.1  # Start with a small step to find an initial range for A
    # Increase A until we are close to the target PB
    while erlang_b_formula(C, A) < target_PB:
        A += step

    # Fine-tune A within tolerance level
    low, high = A - step, A
    while high - low > tolerance:
        mid = (low + high) / 2
        if erlang_b_formula(C, mid) < target_PB:
            low = mid
        else:
            high = mid

    return (low + high) / 2

# Example: Find A for C = 57 channels and a blocking probability of 2%
C = 20
target_PB = 0.05
A = find_traffic_intensity(C, target_PB)
print(f"Traffic Intensity (A) for C={C} and PB={target_PB*100}%: {A:.2f} Erlangs")
