# Image to VHDL/Image to C Array Converter Tools

A basic Python script to convert an image into a set of VHDL constants or a C array.

## Installation

Clone the repository to a known path and ensure that Python3 is installed. You will need the `PIL` image library if it is not already installed.

## Usage

To use, run `img_to_vhdl.py` in a Python3 environment. The tool will fetch the default image from the `/images` directory, run the conversion, and export the constants in a `.txt` file within the `/exports` folder.

To convert another image, change the `path` variable in the Python script to the path of your image.

The same process applies to `img_to_c_array.py`.

## Credits

All images included are Creative Commons 0 and are only used for demonstration purposes.
