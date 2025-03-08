#Creating an interface so that we can add other compression algorithms as well if required. For this assignment, I am considering only RLE.
from abc import ABC, abstractmethod
class Compressor(ABC):
    @abstractmethod
    def compress(self, data):
        pass
    @abstractmethod
    def decompress(self, data):
        pass

class RLECompressor(Compressor):
    def compress(self, data):
        if not data:
            return data
        compr = bytearray()
        counter = 1
        prev_data = data[0]
        for i in range(1,len(data)):
            # if data is repeated in series, increase the counter how many times its been repeated. 
            if data[i] == prev_data:
                counter += 1
            else:
                #if previous data is not same as current, add previously repeated data along with its counter value and reset counter for its new data. 
                compr.append(counter)
                compr.append(prev_data)
                prev_data = data[i]
                counter = 1 
        compr.append(counter)
        compr.append(prev_data)
        return compr
    
    def decompress(self, compressed_data):
        if not compressed_data:
            return compressed_data
        decompressed_data = bytearray()
        if not compressed_data or len(compressed_data) % 2 != 0:
            return decompressed_data
        for i in range(0, len(compressed_data), 2):
            count = compressed_data[i]
            byte = compressed_data[i + 1]
            decompressed_data.extend([byte] * count)
        return bytes(decompressed_data)  