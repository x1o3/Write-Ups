from PIL import Image
import numpy as np

def extract_embedded_data(stego_image_path):
    stego_img = Image.open(stego_image_path).convert("RGB")
    width, height = stego_img.size

    # Create an array to store the extracted 2-bit data
    extracted_data = np.zeros((height, width, 3), dtype=np.uint8)

    for y in range(height):
        for x in range(width):
            r, g, b = stego_img.getpixel((x, y))
            # Extract the 2 LSBs from each color channel
            extracted_data[y, x, 0] = r & 0b00000011
            extracted_data[y, x, 1] = g & 0b00000011
            extracted_data[y, x, 2] = b & 0b00000011

    return extracted_data

def decode_array(encoded_array):
    height, width, channels = encoded_array.shape
    original_width = (width * 2) // 4  # Decode back to the original width of the secret image
    decoded_array = np.zeros((height, original_width, channels), dtype=np.uint8)

    for c in range(channels):
        for y in range(height):
            bit_buffer = 0
            bits_in_buffer = 0
            original_x = 0
            for x in range(width):
                bit_buffer = (bit_buffer << 2) | encoded_array[y, x, c]  # Combine the 2 LSBs
                bits_in_buffer += 2

                while bits_in_buffer >= 4:
                    bits_in_buffer -= 4
                    decoded_array[y, original_x, c] = (bit_buffer >> bits_in_buffer) & 0b1111  # Extract the 4 MSBs
                    original_x += 1

    return decoded_array

def reconstruct_image(decoded_array, output_path):
    height, width, channels = decoded_array.shape
    reconstructed_img = Image.new("RGB", (width, height))

    for y in range(height):
        for x in range(width):
            # Shift the 4 MSBs back to the higher bits
            r = (decoded_array[y, x, 0] << 4) & 0b11110000
            g = (decoded_array[y, x, 1] << 4) & 0b11110000
            b = (decoded_array[y, x, 2] << 4) & 0b11110000
            reconstructed_img.putpixel((x, y), (int(r), int(g), int(b)))

    reconstructed_img.save(output_path, "PNG")
    return reconstructed_img

def main():
    stego_image_path = r'./Images/fractured_faction.png'
    output_image_path = r'./Images/decoded.png'

    embedded_data = extract_embedded_data(stego_image_path)
    decoded_array = decode_array(embedded_data)
    reconstructed_image = reconstruct_image(decoded_array, output_image_path)

    print(f"Decoded image saved to {output_image_path}")

if __name__ == "__main__":
    main()
