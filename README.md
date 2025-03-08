# Overview
RLE Algorithm to compress and decompress a given data buffer of bytes.

## Repository Structure
```
Data-Compression/
├── .github/workflows/manual.yaml  # Trigger pytest on test_data_compression on any merge to main
├── data_compress.py          # Compression interface with RLE implemented
├── test_data_compression.py  # Tests using pytest for RLE functionality
├── input_data.py             # Test data, add input data to the test_data dict variable
├── test_validation_files/    # Contains uncompressed and compressed data for validation
├── README.md                 # Documentation of the project
├── requirements.txt          # List of required libraries for the project
├── .gitignore                # Files to exclude from version control

```

## To use this locally,
- git clone https://github.com/adarshkoppamanjunath/data_compression.git
- Install Python and pip.
- Run `pip install -r requirements.txt` from `data_compression` folder.
- Run `pytest --tb=line --disable-warnings` from `data_compression` folder.

## To use it as container,
- You need to have docker installed.
- Run `docker build -t data_compression .` from `data_compression` folder.
- Run `docker run --rm data_compression` from `data_compression` folder.

## GitHub Action
- Manually trigger .github/workflows/manual.yaml  to see the results


