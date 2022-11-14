#-------------------------------------------------------------------------------------------------
#
#   IMAGE TO VHDL CONVERSION SCRIPT
#
#   Created by Chris Major
#   11/14/22
#
#   A Python script that can convert an image into a VHDL ROM component
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
path = "bird_01__32x32.png"

# Open the image
image = Image.open( "images/" + path )
pixels = image.load()

# Set image limits
x_max, y_max = image.size
#x_max = 32
#y_max = 32

print(pixels)

# Create and open the output file
output_file_name = "exports/" + path[:-4] + ".txt"
output = open( output_file_name, "w" )

# Create dimension constants for image
output.write( "constant c_WIDTH : integer := " + str(x_max) + "\n" )
output.write( "constant c_HEIGHT : integer := " + str(y_max) + "\n\n" )

# Create a type for the array
output.write( "type t_image_array is array ( 0 to (c_HEIGHT - 1), 0 to (c_WIDTH - 1) ) of std_logic_vector( (12 - 1) downto 0);\n\n" )

# Create the array header
output.write( "signal r_image_data	: t_image_array := (\n" )

# Print status message
print( "Converting image ..." )

# Iterate through the columns
for y in range(y_max):
    
    output.write( "\t\t( " )
    
    # Iterate through the rows
    for x in range(x_max):

        # Grab the pixel data
        r, g, b, a = pixels[x, y]
        val = "{:02x}{:02x}{:02x}".format( r, g, b)

        # Convert into a hex value
        hex = "x\"" + val[0] + val[2] + val[4] + "\""
        print( "\t" + val + " --> " + hex )

        # Check if current pixel is at the end of the row
        if x == (x_max - 1):
            output.write( hex + " " )
        else:
            output.write( hex + ", " )

    # Check if current pixel is at the end of the column
    if y == (y_max - 1):
        output.write( ")\n" )
    else:
        output.write( "),\n" )

# Write end of file
output.write( ");\n" )

# Print final message
print( "Image conversion completed!" )

#-------------------------------------------------------------------------------------------------
# END OF CODE
#-------------------------------------------------------------------------------------------------