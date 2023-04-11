#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    ifstream input("image.png", ios::binary); // Replace "image.png"(brain tumor file) with your image file name
    if (input)
    {
        // Get file size
        input.seekg(0, ios::end);
        int size = input.tellg();
        input.seekg(0, ios::beg);

        // Allocate buffer
        char* buffer = new char[size];

        // Read file into buffer
        input.read(buffer, size);

        // Process image data here
        // 

        // Free buffer
        delete[] buffer;
    }
    else
    {
        cout << "Error opening file" << endl;
    }

    return 0;
}
