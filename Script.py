import os
import requests
from concurrent.futures import ThreadPoolExecutor
import time

MAX_RETRIES = 3
RETRY_DELAY = 1  # Delay between retries in seconds

def download_file(year, output_directory):
    base_url = "http://noaa-ghcn-pds.s3.amazonaws.com/csv.gz/"
    file_name = f"{year}.csv.gz"
    s3_url = base_url + file_name
    local_path = os.path.join(output_directory, file_name)
    
    if os.path.exists(local_path) and os.path.getsize(local_path) > 0:
        print(f"Skipping {file_name}. Already exists in {output_directory}")
        return
    
    retries = 0
    while retries < MAX_RETRIES:
        try:
            response = requests.get(s3_url)
            if response.status_code == 200 and len(response.content) > 0:
                with open(local_path, 'wb') as f:
                    f.write(response.content)
                print(f"Downloaded {file_name} to {output_directory}")
                return  # Exit function after successful download
            else:
                print(f"Error downloading {file_name}: Invalid content size. Retrying...")
                retries += 1
                time.sleep(RETRY_DELAY)
        except Exception as e:
            print(f"Error downloading {file_name}: {e}. Retrying...")
            retries += 1
            time.sleep(RETRY_DELAY)
    
    print(f"Failed to download {file_name} after {MAX_RETRIES} retries")
    if os.path.exists(local_path):
        os.remove(local_path)
        print(f"Deleted {file_name}")

def download_missing_files(year_range, output_directory):
    with ThreadPoolExecutor() as executor:
        executor.map(lambda year: download_file(year, output_directory), range(year_range[0], year_range[1] + 1))

# Example usage:
year_range = (1763, 2024)  # Change this to the desired year range
output_directory = "data"  # Change this to the desired output directory

if not os.path.exists(output_directory):
    os.makedirs(output_directory)

download_missing_files(year_range, output_directory)
