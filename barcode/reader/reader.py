import cv2
from pyzbar import pyzbar

def scan_barcode_from_image(image_path):
    # Read the image from the provided file path
    image = cv2.imread(image_path)
    # Decode barcodes from the image using pyzbar
    barcodes = pyzbar.decode(image)
    # Iterate through detected barcodes and extract data from the barcode 
    for barcode in barcodes:
        # uses UTF-8 encoding
        barcode_data = barcode.data.decode("utf-8")
        barcode_type = barcode.type
        print("Barcode Data:", barcode_data)
        print("Barcode Type:", barcode_type)

scan_barcode_from_image("barcode.png")

#

def scan_barcode_from_webcam():
    # Initialize video capture from the default webcam (index 0)
    video_capture = cv2.VideoCapture(0)

    while True:
        # Get a frame from the webcam stream
        _, frame = video_capture.read()

        # Decode barcodes in the frame
        barcodes = pyzbar.decode(frame)

        # Process detected barcodes
        for barcode in barcodes:
            # Extract barcode data and type and print them
            barcode_data = barcode.data.decode("utf-8")
            barcode_type = barcode.type
            print("Barcode Data:", barcode_data)
            print("Barcode Type:", barcode_type)

        # Check for exit condition: Press 'q' to quit the loop
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    # Release video capture and close OpenCV windows
    video_capture.release()
    cv2.destroyAllWindows()


scan_barcode_from_webcam()

