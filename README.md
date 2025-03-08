# Overview
RLE Algorithm to compress and decompress a given data buffer of bytes.

## Repository Structure
Data-Compression/ 
│ │── data_compress.py # Compression interface with RLE implemented. 
│ │── test_data_compression.py # pytest used to test RLE
│ │── input_data.py # add your testdata here. Append input to test_data dict variable. 
│── test_validation_files/ # Consists file for uncompressed and compressed data.
│── README.md # Project documentation
│── requirements.txt # Required libraries
│── .gitignore # Files to exclude from git repo
│── .dockerfile # To create image and run it in container. 

## To use this locally,
- git clone https://github.com/adarshkoppamanjunath/data_compression.git
- Install Python and pip.
- Run `pip install -r requirements.txt` from `data_compression` folder.
- Run `pytest --tb=line --disable-warnings` from `data_compression` folder.

## To use it as container,
- You need to have docker installed.
- Run `docker build -t data_compression .` from `data_compression` folder.
- Run `docker run --rm data_compression` from `data_compression` folder.


