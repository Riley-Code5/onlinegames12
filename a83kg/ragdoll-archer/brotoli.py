import brotli

try:
    with open('b3397c29f6878557c1c614cbf9e196ea.wasm.unityweb', 'rb') as f_in:
        compressed_data = f_in.read()

    decompressed_data = brotli.decompress(compressed_data)

    with open('decompressed.wasm', 'wb') as f_out:
        f_out.write(decompressed_data)

    print("Successfully decompressed to decompressed.wasm")

except brotli.error as e:
    print(f"Brotli decompression error: {e}")
except FileNotFoundError:
    print("Error: The file 'b3397c29f6878557c1c614cbf9e196ea.wasm.unityweb' was not found.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")