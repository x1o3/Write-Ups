#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

uint8_t decodeBit(uint8_t bit) {
    return bit ^ 1;
}

uint8_t extractBitFromChannel(FILE *imageFile, size_t row, size_t col, size_t channel, size_t imageWidth) {
    size_t pixelOffset = (row * imageWidth + col) * 3 + channel;
    fseek(imageFile, pixelOffset, SEEK_SET);
    uint8_t channelValue;
    fread(&channelValue, 1, 1, imageFile);

    return channelValue & 0x01;
}

int getImageDimensions(FILE *imageFile, size_t *width, size_t *height) {
    fseek(imageFile, 18, SEEK_SET);
    fread(width, sizeof(uint32_t), 1, imageFile);
    fread(height, sizeof(uint32_t), 1, imageFile);
    return 0;
}

int main() {
    FILE *imageFile = fopen("image.bmp", "r");
    if (imageFile == NULL) {
        perror("Error opening image file");
        return 1;
    }

    FILE *outputFile = fopen("output.txt", "w");
    if (outputFile == NULL) {
        perror("Error opening output file");
        fclose(imageFile);
        return 1;
    }

    size_t imageWidth, imageHeight;
    if (getImageDimensions(imageFile, &imageWidth, &imageHeight) != 0) {
        perror("Error reading image dimensions");
        fclose(imageFile);
        fclose(outputFile);
        return 1;
    }

    size_t row = 0; 
    size_t col = 0; 
    size_t channel = 0; 
    size_t bitIndex = 0; 

    uint8_t byte = 0; 

    while (row < imageHeight) {
        for (int i = 7; i >= 0; i--) { 
            if (row >= imageHeight) {
                break;
            }

            uint8_t bit = extractBitFromChannel(imageFile, row, col, channel, imageWidth); 

            if (bitIndex % 2 == 1) {
                bit = decodeBit(bit);
            }

            byte |= (bit << i);  

            channel = (channel + 1) % 3;  
            if (channel == 0) {
                col++;
                if (col >= imageWidth) {
                    col = 0;
                    row++;
                }
            }

            bitIndex++;  
        }

        fputc(byte, outputFile);
        byte = 0; 

        row += 2;
    }

    fclose(imageFile);
    fclose(outputFile);

    printf("Data extracted successfully.\n");
    return 0;
}
