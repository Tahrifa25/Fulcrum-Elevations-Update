from update_elevation import updating_elevation
from convert_resolution import arcseconds_to_meters

def main():
    updating_elevation()
    
    resolution = 1  # arc-seconds
    latitude = 36.5  # example latitude (e.g., Nashville, TN)
    accuracy = arcseconds_to_meters(resolution, latitude)
    print(f"Horizontal accuracy: {accuracy['horizontal_accuracy_m']} meters")
    print(f"Vertical accuracy: {accuracy['vertical_accuracy_m']} meters")

if __name__ == "__main__":
    main()

    
