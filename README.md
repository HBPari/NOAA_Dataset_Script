# NOAA Dataset Download Script

This script is designed to automate the process of downloading meteorological data files from the NOAA's Global Historical Climatology Network (GHCN). The GHCN data is vital for climate research and analysis, and this tool facilitates easy and systematic access to the files, which span from the year 1763 to the present.

## Prerequisites

Before you begin, you will need:
- Python 3.x
- Requests library

## Installation

First, clone this repository to your local system:

```bash
git clone https://github.com/yourusername/NOAA_Dataset_Script.git
cd NOAA_Dataset_Script
```

Install the required packages using pip:

```bash
pip install requests
```

## Usage

To use the script, you will need to:
1. Set the `year_range` in the script to the range of years you are interested in downloading.
2. Configure the `output_directory` to where you want the files saved.
3. Execute the script:

```bash
python download_script.py
```

The script performs checks to avoid re-downloading existing files that are complete, making it efficient in managing data storage.

## Script Details

- **`download_file(year, output_directory)`**: Handles downloading a file for a specific year. It includes error handling for failed downloads and retries.
- **`download_missing_files(year_range, output_directory)`**: Manages the concurrent download of files for the specified range of years to speed up the process.

## Contributing

If you're interested in contributing to this project:
1. Fork the repository.
2. Create a new branch for your feature.
3. Add your improvements.
4. Submit a pull request.

Contributions, issues, and feature requests are welcome!

## License

This project is open source and available under the [MIT License](LICENSE.md).

## Contact

For any questions or comments, please open an issue in this repository.
