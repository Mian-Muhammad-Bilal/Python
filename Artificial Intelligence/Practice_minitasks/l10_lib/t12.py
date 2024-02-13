import zlib


def compress_and_decompress(input_string):
    compressed_data = zlib.compress(input_string.encode())

    decompressed_data = zlib.decompress(compressed_data)
    original_string = decompressed_data.decode()

    return original_string


input_string = "sample string."
result = compress_and_decompress(input_string)

print("Original String:", input_string)
print("Compressed and Decompressed String:", result)
