#add your testdata here
test_data = {
    "test 1": bytes([]),  
    # Edge Case: Empty input (Boundary)

    "test 2": bytes([0x11]),  
    # Edge Case: Only one byte (Boundary)

    "test 3": bytes([0x11, 0x11]),  
    # Edge Case: Smallest possible RLE compression

    "test 4": bytes([0x11, 0x22]),  
    # Edge Case: No compression possible (Boundary)

    "test 5": bytes([0x11] * 100 + [0x22] * 80 + [0x33] * 60),  
    # Long repeating sequences (Best case for RLE)

    "test 6": bytes([0x11, 0x11, 0x22, 0x22, 0x33, 0x33, 0x44, 0x44] * 10),  
    # Short repeated blocks (Still good for RLE)

    "test 7": bytes([0x11] * 40 + [0x22] * 5 + [0x33] * 25 + [0x44] * 10 + [0x55] * 8),  
    # Combination of long and short repeats

    "test 8": bytes([0x77] * 255),  
    # Edge Case: Maximum RLE count (Boundary, 255 repetitions)

    "test 9": bytes([0x7F] * 50),  
    # Edge Case: Highest value byte in range

    "test 10": bytes([0x11, 0x22] * 50),  
    # Alternating pattern

    "test 11": bytes([0x11, 0x55, 0x77, 0x33, 0x44, 0x66, 0x22, 0x99, 0xAA, 0xBB, 0xCC, 0xDD] * 10)  
    # Completely varied 
}
