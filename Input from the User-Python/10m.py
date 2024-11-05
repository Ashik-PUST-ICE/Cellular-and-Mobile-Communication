import math

def calculate_erlang_c(R, N, Au):
    # Calculate area covered per cell
    area = round(2.5981 * R**2)  # Area in sq km
    C = N / 4  # Number of channels per cell (assuming a 4-cell system)

    # Traffic intensity at C=15, GOS=0.05
    A = 9  # Given traffic intensity

    # Question (a)
    U = A / Au  # Number of users
    U_per = U / area  # Number of users per square km

    print(f"(a) Number of users per square km: {int(U_per)} users/sq km\n")

    # Question (b)
    lamda = 1  # Lambda = 1 call/hour
    H = (Au / lamda) * 3600  # Holding time in seconds
    t = 10  # Time in seconds
    Prb = math.exp(-(C - A) * t / H)  # Probability that a delayed call will wait more than t seconds

    print(f"(b) The probability that a delayed call will have to wait: {Prb * 100:.2f}%\n")

    # Question (c)
    Prc = 0.05 * Prb  # Probability that a call is delayed more than 10 seconds
    print(f"(c) The probability that a call will be delayed: {Prc * 100:.2f}%\n")

# Main loop for user input
while True:
    try:
        # Collect user inputs
        R = float(input("Enter the cell radius in km: "))
        N = int(input("Enter the total number of channels: "))
        Au = float(input("Enter the traffic per user in Erlangs: "))

        # Calculate and display results
        calculate_erlang_c(R, N, Au)

    except ValueError:
        print("Invalid input. Please enter numeric values.")

    # Prompt to continue or exit
    continue_input = input("Do you want to calculate again? (yes/no): ").strip().lower()
    if continue_input != 'yes':
        break


# 10. A hexagonal cell within a 4-cell system has a radius of 1.387 km. A total of 60 
# channels are used within the entire system. If the load per user is 0.029 Erlangs, and 
# λ= call/hour, compute the following for an Erlang C system that has a 5% probability 
# of a delayed call- 
# a) How many users per square kilometer will this system support? 
# b) What is the probability that a delayed call will have to wait for more than 10s? 
# c) What is the probability that a call will be delayed for more than 10 seconds? 