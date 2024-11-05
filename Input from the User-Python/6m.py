import math

def power_conversion(transmitter_power_watts):
    power_mw = transmitter_power_watts * 1000
    power_dbm = 10 * math.log10(power_mw)
    power_dbw = 10 * math.log10(transmitter_power_watts)
    return power_dbm, power_dbw

def received_power(distance_m, transmitter_power_w, gt, gr, frequency_hz):
    c = 3 * 10**8  # Speed of light in m/s
    wavelength = c / frequency_hz
    pr = (transmitter_power_w * gt * gr * (wavelength**2)) / ((4 * math.pi * distance_m)**2)
    pr_dbm = 10 * math.log10(pr * 1000)
    return pr_dbm

def received_power_at_distance(pr_100_dbm, distance_m, reference_distance_m):
    path_loss = 20 * math.log10(distance_m / reference_distance_m)
    pr_new_dbm = pr_100_dbm - path_loss
    return pr_new_dbm

while True:
    # User inputs
    transmitter_power_w = float(input("Enter the transmitter power in watts: "))
    gt = float(input("Enter the transmitter gain (in linear scale, e.g., 1 for unity gain): "))
    gr = float(input("Enter the receiver gain (in linear scale, e.g., 1 for unity gain): "))
    frequency_hz = float(input("Enter the carrier frequency in MHz: ")) * 10**6  # Convert MHz to Hz

    # Convert power
    power_dbm, power_dbw = power_conversion(transmitter_power_w)

    # Calculate received power at 100 m
    distance_100_m = 100
    received_power_100_dbm = received_power(distance_100_m, transmitter_power_w, gt, gr, frequency_hz)

    # Calculate received power at 10 km
    reference_distance_m = 100
    distance_10_km = 10000
    received_power_10_km_dbm = received_power_at_distance(received_power_100_dbm, distance_10_km, reference_distance_m)

    # Display results
    print(f"\nFinal Results:")
    print(f"(a) Transmitter power P_t in dBm: {power_dbm:.1f} dBm")
    print(f"(b) Transmitter power P_t in dBW: {power_dbw:.1f} dBW")
    print(f"(c) Received power P_r at 100 m in dBm: {received_power_100_dbm:.1f} dBm")
    print(f"(d) Received power P_r at 10 km in dBm: {received_power_10_km_dbm:.1f} dBm")
    
    # Check if the user wants to continue
    continue_choice = input("\nDo you want to perform another calculation? (yes/no): ").strip().lower()
    if continue_choice != 'yes':
        break


# 6. If a transmitter produces 50 watts of power, express the transmit power in units of  
# a) dBm,   
# and b) dBW. 
# If 50 watts is applied to a unity gain antenna with a 900 MHz carrier frequency,  
# a) Find the received power in dBm at a free space distance of 100 m from the 
# antenna,  
# b) What is P (10 km)?  
# Assume unity gain for the receiver antenna.