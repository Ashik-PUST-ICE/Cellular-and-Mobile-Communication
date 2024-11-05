import math

# Constants
c = 3 * 10**8  # Speed of light in m/s

# Function to perform calculations based on user input
def calculate_antenna_parameters():
    # User inputs
    f = float(input("Enter frequency in MHz: "))
    g = float(input("Enter gain of antenna in dB: "))
    
    # Question (a)
    # Convert gain from dB to linear scale
    gain_linear = 10 ** (g / 10)  # Gain in linear scale

    # Calculate wavelength in meters
    lambda_ = c / (f * 10**6)

    # Calculate length of the antenna (1/4 of wavelength)
    L = lambda_ / 4  # Length of the antenna in meters

    # Display results for part (a)
    print('For (a)')
    print('---------')
    print(f'Length of the antenna: {L * 100:.2f} cm')  # Convert to cm
    print(f'Gain of the antenna: {gain_linear:.2f} = {g:.2f} dB\n')

    # Question (b)
    d = float(input("Enter T-R separation distance in meters: "))
    E0 = float(input("Enter electric-field strength in V/m (e.g., 0.001): "))  # Directly input 0.001 instead of 10**-3
    d0 = float(input("Enter reference distance in meters: "))
    ht = float(input("Enter height of transmitting antenna in meters: "))
    hr = float(input("Enter height of receiving antenna in meters: "))

    # Electric Field Calculation
    Er_d = (2 * E0 * d0 * 2 * math.pi * ht * hr) / (lambda_ * d**2)  # Electric Field in V/m

    # Effective Aperture Calculation
    Ae = (gain_linear * lambda_**2) / (4 * math.pi)  # Effective Aperture in m²

    # Received Power Calculation
    Pr = (Er_d**2 / (120 * math.pi)) * Ae  # Received power in watts
    Pr_dB = 10 * math.log10(Pr)  # Received power in dBW
    Pr_dBm = Pr_dB + 30  # Convert to dBm

    # Display results for part (b)
    print('For (b)')
    print('---------')
    print(f'Electric Field, Er(d): {Er_d:.9f} V/m')
    print(f'Effective Aperture, Ae: {Ae:.3f} m²')
    print(f'Received power at {d} meters distance: {Pr_dB:.2f} dBW')
    print(f'Received power at {d} meters distance: {Pr_dBm:.2f} dBm\n')

# Main loop for multiple inputs
while True:
    calculate_antenna_parameters()
    
    # Prompt to continue or exit
    continue_input = input("Do you want to calculate for another antenna configuration? (yes/no): ").strip().lower()
    if continue_input != 'yes':
        break



# 9. A mobile is located 5 km away from a base station and uses a vertical λ /4 monopole 
# antenna with a gain of 2.55 dB to receive cellular 3 radio signals. The E-field at 1 km 
# from the transmitter is measured to be V/m. The carrier frequency used for this 
# system is 900 MHz. 
# a) Find the length and the gain of the receiving antenna. 
# b) Find the received power at the mobile using the 2-ray ground reflection model 
# assuming the height of the transmitting antenna is 50 m and the receiving 
# antenna is 1.5m above ground.