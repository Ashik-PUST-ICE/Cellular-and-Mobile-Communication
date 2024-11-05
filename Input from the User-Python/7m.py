import math

def calculate_path_loss(fc, hte, hre, d):
    # Calculate the correction factor for effective mobile antenna height
    a_hre = 3.2 * (math.log10(11.75 * hre)) ** 2 - 4.97

    # Calculate path loss using the Okumura-Hata model
    path_loss = (69.55 +
                 26.16 * math.log10(fc) -
                 13.82 * math.log10(hte) -
                 a_hre +
                 (44.9 - 6.55 * math.log10(hte)) * math.log10(d))
    
    return path_loss

while True:
    # Input values from the user
    try:
        fc = float(input("Enter the frequency (in MHz): "))  # Frequency in MHz
        hte = float(input("Enter the base station height (in meters): "))  # Base station height in meters
        hre = float(input("Enter the mobile station height (in meters): "))  # Mobile station height in meters
        d = float(input("Enter the distance (in kilometers): "))  # Distance in kilometers

        # Calculate path loss
        path_loss = calculate_path_loss(fc, hte, hre, d)
        print(f"The path loss is approximately {path_loss:.2f} dB.")
    except ValueError:
        print("Please enter valid numerical values.")

    # Ask if the user wants to continue or exit
    continue_input = input("Do you want to calculate path loss for another set of values? (yes/no): ").strip().lower()
    if continue_input != 'yes':
        break


# 7. Determine the path loss of a 900MHz cellular system in a large city from a base 
# station with the height of 100m and mobile station installed in a vehicle with antenna 
# height of 2m. The distance between mobile and base station is 4Km.