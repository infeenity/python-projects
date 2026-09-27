# Python Image Toolkit

A simple, interactive Python utility for resizing, compressing and
converting images using Pillow.

I originally built separate scripts while learning how Python could
resize images and reduce their file sizes. I then combined those
experiments into this reusable interactive toolkit.

## Features

The toolkit can:

- Resize an image while preserving its aspect ratio
- Resize an image to exact dimensions
- Compress an image below a user-specified target file size
- Resize and compress an image in one operation
- Convert an image to grayscale

The user enters the required dimensions and target file size when the
program runs — there is no need to edit the Python source code.

## Requirements

- Python 3
- Pillow

Install Pillow with:

    pip install Pillow

Or, after downloading this project:

    pip install -r requirements.txt

## How to use

Run:

    python image_toolkit.py

The program will ask for the image you want to process.

For example:

    Enter the path or filename of the image: photo.jpg

You can then choose:

    1 - Resize image
    2 - Compress image
    3 - Resize AND compress image
    4 - Convert image to grayscale

## Example — resize and compress

Suppose you select:

    3 - Resize AND compress image

The program asks:

    Enter target width in pixels: 800
    Enter target height in pixels: 800

You can then choose whether to preserve the original aspect ratio or
force the image to the exact dimensions.

For example:

    1 - Keep aspect ratio
    2 - Exact dimensions

Finally, enter the maximum desired file size:

    Enter maximum output file size in KB: 200

The program processes the image and reports the resulting dimensions,
file size and JPEG quality.

## Understanding the resize modes

### Keep aspect ratio

The image is fitted inside the maximum width and height supplied by
the user without changing its proportions.

For example:

    Original: 2400 x 1600
    Maximum:   800 x 800
    Result:    800 x 533

This avoids distorting the image.

### Exact dimensions

The image is forced to the exact width and height supplied.

For example:

    Requested: 200 x 400
    Result:    200 x 400

This may distort the image if the requested proportions differ from
the original.

## Compression

For compression, the program starts with a high JPEG quality and
progressively reduces the quality until the image is below the target
file size.

If the requested size cannot be achieved without going below the
minimum JPEG quality, the program tells the user rather than
automatically changing the image dimensions.

The user can then choose to:

- increase the target file size, or
- resize the image to smaller dimensions and try again.

## Output files

The program automatically creates an output filename based on the
operation performed.

Examples:

    photo_resized.jpg
    photo_compressed.jpg
    photo_resized_compressed.jpg
    photo_grayscale.jpg

The original image is not overwritten.

## What I learned

Building this project helped me practise:

- Importing and using an external Python library
- Pillow image processing
- User input with `input()`
- Variables and data types
- Conditional logic
- `while` loops
- Input validation
- File handling
- `io.BytesIO`
- Image dimensions and aspect ratios
- JPEG quality and compression
- Checking files with the `os` module

## Future improvements

As I continue learning Python, possible improvements include:

- Refactoring the program into functions
- Command-line arguments
- Batch image processing
- Additional output formats
- Improved error handling
- A graphical user interface

## Author

Deb Das

Part of my ongoing journey back into hands-on technology and software
development.
