import os

def rename_chirpstack_in_vendors(vendors_dir):
    if not os.path.isdir(vendors_dir):
        print(f"Directory '{vendors_dir}' not found or is not a directory.")
        return

    for vendor in os.listdir(vendors_dir):
        vendor_path = os.path.join(vendors_dir, vendor)
        if not os.path.isdir(vendor_path):
            continue

        for device in os.listdir(vendor_path):
            device_path = os.path.join(vendor_path, device)
            if not os.path.isdir(device_path):
                continue

            chirpstack_path = os.path.join(device_path, "ChirpStack")
            if os.path.isdir(chirpstack_path):
                new_chirpstack_path = os.path.join(device_path, "CHIRPSTACK")
                os.rename(chirpstack_path, new_chirpstack_path)
                print(f"Renamed: {chirpstack_path} -> {new_chirpstack_path}")

if __name__ == "__main__":
    vendors_directory = "VENDORS"
    rename_chirpstack_in_vendors(vendors_directory)