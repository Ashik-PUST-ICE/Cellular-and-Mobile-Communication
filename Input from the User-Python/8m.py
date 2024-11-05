import math

def calculate_path_loss(fc, hb, d):
    # Calculate the T-R separation distance in km
    d_km = math.sqrt(20**2 + 30**2) / 1000  # Convert meters to kilometers

    # Calculate path loss using the Okumura-Hata model
    path_loss = (135.41 +
                 12.49 * math.log10(fc) -
                 4.99 * math.log10(hb) +
                 (46.84 - 2.34 * math.log10(hb)) * math.log10(d_km))
    
    return path_loss

while True:
    # Input values from the user
    try:
        fc = float(input("Enter the frequency (in GHz, e.g., 1.8): "))  # Frequency in GHz
        hb = float(input("Enter the base station height (in meters): "))  # Base station height in meters

        # Calculate path loss
        path_loss = calculate_path_loss(fc, hb, 0)  # d is calculated within the function
        print(f"The path loss is approximately {path_loss:.2f} dB.")
    except ValueError:
        print("Please enter valid numerical values.")

    # Ask if the user wants to continue or exit
    continue_input = input("Do you want to calculate path loss for another set of values? (yes/no): ").strip().lower()
    if continue_input != 'yes':
        break


# 8. Determine the path loss between base station (BS) and mobile station (MS) of a 
# 1.8GHz PCS system operating in a high-rise urban area. The MS is located in a 
# perpendicular street to the location of the BS. The distances of the BS and MS to the 
# corner of the street are 20 and 30 meters, respectively. The base station height is 20m. 