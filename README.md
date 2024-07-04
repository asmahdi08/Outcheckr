# Outcheckr

Outcheckr is a powerful tool for enumerating outbound links from web pages. It can fetch all outbound links from a given URL or from multiple URLs listed in a file. This tool is useful for web scraping, SEO analysis, bug bounty hunting.

(use for educational purposes only.)

## Features

- Fetch outbound links from a single URL.
- Fetch outbound links from multiple URLs listed in a file.
- Supports output in coloured or plain text.
- Real-time display of results with verbosity option.
- Save results to a specified output file.

## Requirements

- Python 3.6 or higher
- Required Python packages (can be installed via `requirements.txt`):

  ```sh
  pip install -r requirements.txt

## Installation
1. Clone the repository:
  
  ```sh
  https://github.com/asmahdi08/Outcheckr.git
  ```

2. Navigate to the project directory:

  ```sh
  cd Outcheckr
  ```

3. Install the required dependencies:

  ```sh
  pip install -r requirements.txt
```

# Usage
## Basic Usage
To use Outcheckr, you can run the following command:

```sh
python outcheckr.py -u <URL> -o <output_file>
```
## Arguments
- -u, --url: URL to check for outbound links. Required.
- -n, --no-color: Output without colors. Optional.
- -v, --verbose: Display results real-time. Optional.
- -o, --output: File to save the results. Required.
## Examples
- Fetch outbound links from a single URL and save to results.txt:

```sh
python outcheckr.py -u https://example.com -o results.txt
```


- Fetch outbound links from a single URL without color output:

```sh
python outcheckr.py -u https://example.com -o results.txt -n
```

- Fetch outbound links from multiple URLs listed in urls.txt and save to results.txt:

```sh
python outcheckr.py -u urls.txt -o results.txt
```

- Display results in real-time:

```sh
python outcheckr.py -u https://example.com -o results.txt -v
```

# License
This project is licensed under the MIT License. See the LICENSE file for details.

# Contributing
We welcome contributions! Please read our Contributing Guide for details on how to get started.

# Contact
If you have any questions or suggestions, feel free to open an issue or email ashfaqsadat2008@gmail.com
