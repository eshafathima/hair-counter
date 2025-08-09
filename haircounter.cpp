#define STB_IMAGE_IMPLEMENTATION
#include "stb_image.h"

#include <iostream>
#include <fstream>
#include <string>
#include <cstdlib>

using namespace std;

// Simple grayscale threshold counting example (very rough)
int count_dark_pixels(unsigned char* data, int w, int h, int channels, int threshold=50) {
    int count = 0;
    for(int i=0; i<w*h; i++) {
        int r = data[i*channels + 0];
        int g = data[i*channels + 1];
        int b = data[i*channels + 2];
        int gray = (r+g+b)/3;
        if(gray < threshold) count++;
    }
    return count;
}

int main() {
    // For simplicity: read entire stdin as raw data (simulate multipart parsing yourself)
    string filedata = /* your multipart parser output here, raw image bytes */;

    // Load image from memory
    int width, height, channels;
    unsigned char* img = stbi_load_from_memory(
        (const unsigned char*)filedata.data(),
        (int)filedata.size(),
        &width, &height, &channels, 3);
    
    if (!img) {
        cout << "{\"error\":\"Failed to load image\"}\n";
        return 1;
    }

    int dark_count = count_dark_pixels(img, width, height, 3);

    stbi_image_free(img);

    cout << "Content-Type: application/json\r\n\r\n";
    cout << "{ \"dark_pixel_count\": " << dark_count << " }\n";

    return 0;
}