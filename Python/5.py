def main():
    # Given values
    total_coverage_area = 1300  # in square miles
    cell_radius = 4  # in miles
    allocated_spectrum = 40_000_000  # in Hz
    channel_width = 60_000  # in Hz
    frequency_reuse_factor = 7  # N
    offered_traffic_per_user = 0.03  # in Erlangs
    
    
    # (a) Calculate the number of cells in the service area
    area_of_cell = 2.5981 * (cell_radius ** 2)  # area in square miles
    number_of_cells = total_coverage_area / area_of_cell
    number_of_cells = int(number_of_cells)  # Use integer value for number of cells

    # (b) Calculate the number of channels per cell
    total_channels_per_cell = allocated_spectrum // (channel_width * frequency_reuse_factor)  # Use integer division

    # (c) Traffic intensity of each cell (already given)
    # This is taken from the Erlang B table based on 95 channels per cell and a 2% GOS
    traffic_intensity_per_cell = 84  # in Erlangs (reference value)
    
    # (d) Calculate the maximum carried traffic
    maximum_carried_traffic = number_of_cells * traffic_intensity_per_cell

    # (e) Calculate the total number of users that can be served for 2% GOS
    total_users = maximum_carried_traffic / offered_traffic_per_user

    # (f) Calculate the number of mobiles per channel
    total_channels = allocated_spectrum // channel_width  # Use integer division
    mobiles_per_channel = total_users / total_channels

    # (g) Calculate the theoretical maximum number of users that could be served at one time by the system
    theoretical_max_users = total_channels_per_cell * number_of_cells

    # Print results
    print(f"a) Number of cells in the service area: {number_of_cells} cells")
    print(f"b) Number of channels per cell: {total_channels_per_cell} channels/cell")
    print(f"c) Traffic intensity of each cell: {traffic_intensity_per_cell} Erlangs/cell")
    print(f"d) Maximum carried traffic: {maximum_carried_traffic:.2f} Erlangs")
    print(f"e) Total number of users that can be served for 2% GOS: {total_users:.0f} users")
    print(f"f) Number of mobiles per channel: {mobiles_per_channel:.2f} mobiles/channel")
    print(f"g) Theoretical maximum number of users that could be served at one time: {theoretical_max_users} users")

if __name__ == "__main__":
    main()
