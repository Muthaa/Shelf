# import EAN13 from barcode module 
from barcode import EAN13 

def method1():
    # Make sure to pass the number as string 
    number = '5901234123457'

    # Now, let's create an object of EAN13 
    # class and pass the number 
    my_code = EAN13(number) 

    # Our barcode is ready. Let's save it. 
    my_code.save("new_code")

import barcode
from the barcode.writer import ImageWriter

def generate_barcode(data, barcode_format, options=None):
    # Get the barcode class corresponding to the specified format     
    barcode_class = barcode.get_barcode_class(barcode_format)
    # Create a barcode image using the provided data and format
    barcode_image = barcode_class(data, writer=ImageWriter())
    # Save the barcode image to a file named "barcode" with the specified options
    barcode_image.save("barcode", options=options)

generate_barcode("MakeUseOf", "code128", options={"foreground":"blue", 
                                                  "center_text": False, 
                                                  "module_width":0.4, 
                                                  "module_height":20})
