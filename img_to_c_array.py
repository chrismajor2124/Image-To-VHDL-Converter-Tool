#-------------------------------------------------------------------------------------------------
#
#   IMAGE TO C ARRAY CONVERSION SCRIPT
#
#   Created by Chris Major
#   1/5/23
#
#   A Python script that can convert an image into a C array of uint32 values
#
#-------------------------------------------------------------------------------------------------


#-------------------------------------------------------------------------------------------------
# LIBRARIES
#-------------------------------------------------------------------------------------------------

from PIL import Image
import binascii


#-------------------------------------------------------------------------------------------------
# MAIN CODE
#-------------------------------------------------------------------------------------------------

# Path to the image (change to the image of your choice!)
path = "moon3_square_light_16x16.png"

# Open the image
image = Image.open( "images/" + path )
pixels = image.load()

# Set image limits
x_max, y_max = image.size

# Print the pixels
print(pixels)

# Create and open the output file
output_file_name = "exports/" + path[:-4] + "_c_array.txt"
output = open( output_file_name, "w" )

# Create dimension constants for image
output.write( "// Array to represent image \"" + path + "\"\n" )

# Create the array header
output.write( "uint32_t " + path[:-4] + "_image[" + str(y_max) + "][" + str(x_max) + "] = " + "\n{\n" )

# Print status message
print( "Converting image ..." )

# Iterate through the columns
for y in range(y_max):
    
    output.write( "\t{ " )
    
    # Iterate through the rows
    for x in range(x_max):

        # Grab the pixel data
        r, g, b, a = pixels[x, y]
        val = "{:02x}{:02x}{:02x}".format( r, g, b)

        # Convert into a hex value of 32 bits
        hex = "0x00" + val.upper()
        print( "\t" + val + " --> " + hex )

        # Check if current pixel is at the end of the row
        if x == (x_max - 1):
            output.write( hex + " " )
        else:
            output.write( hex + ", " )

    # Check if current pixel is at the end of the column
    if y == (y_max - 1):
        output.write( "}\n" )
    else:
        output.write( "},\n" )

# Write end of file
output.write( "};\n" )

# Print final message
print( "Image conversion completed!" )

#-------------------------------------------------------------------------------------------------
# END OF CODE
#-------------------------------------------------------------------------------------------------