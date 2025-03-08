#In this file you can test the alogirm by passing different test input data ( test data needs to be updated in input_data.py file.)
import pytest
from data_compress import RLECompressor
from input_data import test_data
import os

"""
  Your submission will be judged based on
- The number of bytes your output uses if saved to file
- Run time
- Scalability
- Maintainability
- Testability
- The compressed data will need to be decompressable. Please ensure that your algorithm allows for a
decompression algorithm to return the buffer to its previous form.

"""

def get_compressed_data(data,method="RLE"):
    if method == "RLE":
        rle_obj = RLECompressor()
        return rle_obj.compress(data)

def get_decompressed_data(compressed_data,method="RLE"):
    if method == "RLE":
        rle_obj = RLECompressor()
        return rle_obj.decompress(compressed_data)
        
def get_all_insights_for_test_data(data_dict, folder="test_validation_files"):
    # saving uncompressed and compressed data to file since its mentioned that output will be saved to a file and consider the file size
    # using RLE compression technique by default. 
    
    if not os.path.exists(folder):
        os.makedirs(folder)
    file_sizes = {}
    for name, data in data_dict.items():
        #create two files one for uncompressed data and other for compressed data
        uncompressed_file = os.path.join(folder, f"{name}_uncompressed.bin")
        compressed_file = os.path.join(folder, f"{name}_compressed.bin")
        
        #get uncompressed file size. 
        with open(uncompressed_file, "wb") as f:
            f.write(data)
        uncompressed_size = os.path.getsize(uncompressed_file)
        
        #get compressed data
        compressed_data = get_compressed_data(data)
        
        #save compressed data to a file and get its size. 
        with open(compressed_file, "wb") as f:
            f.write(compressed_data)
        compressed_size = os.path.getsize(compressed_file)
        
        #decompress to check integrity. 
        decompressed_data = get_decompressed_data(compressed_data)

        # store test details 
        file_sizes[name] = {
            "uncompressed_size": uncompressed_size,
            "compressed_size": compressed_size,
            "integrity_test": data == decompressed_data
        }
        print(f"Saved '{name}': {uncompressed_size} bytes -> {compressed_size} bytes | Integrity: {file_sizes[name]['integrity_test']}")
    return file_sizes


@pytest.fixture(scope="module")
def compression_results():
    return get_all_insights_for_test_data(test_data)

@pytest.mark.parametrize("data_name", test_data.keys())
def test_compression_sizes(data_name, compression_results):
    sizes = compression_results[data_name]
    assert sizes["compressed_size"] <= sizes["uncompressed_size"], (
        f"Compressed file for {data_name} is larger than uncompressed!: {sizes}"
    )
    
@pytest.mark.parametrize("data_name", test_data.keys())
def test_data_integrity(data_name, compression_results):
    sizes = compression_results[data_name]
    assert sizes["integrity_test"], f"Data corruption detected for {data_name}!"