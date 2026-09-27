from PIL import Image
import io
import os


# ============================================================
# PYTHON IMAGE TOOLKIT
# ============================================================
#
# A beginner-friendly image utility that can:
#
# 1. Resize an image
# 2. Compress an image to a target file size
# 3. Resize AND compress an image
# 4. Convert an image to grayscale
#
# The user enters the required dimensions and file size
# when the program runs.
# ============================================================


print()
print("================================")
print("      PYTHON IMAGE TOOLKIT")
print("================================")
print()


# ============================================================
# GET INPUT FILE
# ============================================================

input_file = input(
    "Enter the path or filename of the image: "
).strip()


# Check whether the file exists

if not os.path.isfile(input_file):
    print()
    print("ERROR: The image file could not be found.")
    print("Please check the filename or path and try again.")
    raise SystemExit


# ============================================================
# CHOOSE OPERATION
# ============================================================

print()
print("What would you like to do?")
print()
print("1 - Resize image")
print("2 - Compress image")
print("3 - Resize AND compress image")
print("4 - Convert image to grayscale")
print()


while True:

    choice = input("Enter your choice (1-4): ").strip()

    if choice in ["1", "2", "3", "4"]:
        break

    print("Please enter 1, 2, 3 or 4.")


# ============================================================
# OPEN IMAGE
# ============================================================

try:
    image = Image.open(input_file)

except Exception as error:
    print()
    print("ERROR: The file could not be opened as an image.")
    print(error)
    raise SystemExit


original_width, original_height = image.size

original_file_size = os.path.getsize(input_file) / 1024


print()
print("--------------------------------")
print("ORIGINAL IMAGE")
print("--------------------------------")

print(
    "Dimensions:",
    original_width,
    "x",
    original_height
)

print(
    "File size:",
    round(original_file_size, 2),
    "KB"
)


# Convert to RGB so the result can be saved as JPEG.
#
# Some images, such as PNG files, may use RGBA colour mode.
# JPEG does not support RGBA.

image = image.convert("RGB")


# ============================================================
# RESIZE
# ============================================================

if choice == "1" or choice == "3":

    print()
    print("--------------------------------")
    print("RESIZE SETTINGS")
    print("--------------------------------")


    # --------------------------------------------------------
    # GET WIDTH
    # --------------------------------------------------------

    while True:

        try:

            target_width = int(
                input("Enter target width in pixels: ")
            )

            if target_width > 0:
                break

            print("Width must be greater than 0.")

        except ValueError:

            print("Please enter a whole number.")


    # --------------------------------------------------------
    # GET HEIGHT
    # --------------------------------------------------------

    while True:

        try:

            target_height = int(
                input("Enter target height in pixels: ")
            )

            if target_height > 0:
                break

            print("Height must be greater than 0.")

        except ValueError:

            print("Please enter a whole number.")


    # --------------------------------------------------------
    # CHOOSE RESIZE MODE
    # --------------------------------------------------------

    print()
    print("How should the image be resized?")
    print()
    print("1 - Keep aspect ratio")
    print("    Fits inside the width and height you entered.")
    print()
    print("2 - Exact dimensions")
    print("    Forces the image to the exact width and height.")
    print("    This may distort the image.")
    print()


    while True:

        resize_mode = input(
            "Enter your choice (1-2): "
        ).strip()

        if resize_mode in ["1", "2"]:
            break

        print("Please enter 1 or 2.")


    # --------------------------------------------------------
    # PERFORM RESIZE
    # --------------------------------------------------------

    if resize_mode == "1":

        image.thumbnail(
            (target_width, target_height),
            Image.Resampling.LANCZOS
        )

    else:

        image = image.resize(
            (target_width, target_height),
            Image.Resampling.LANCZOS
        )


# ============================================================
# GRAYSCALE
# ============================================================

if choice == "4":

    image = image.convert("L")


# ============================================================
# CREATE OUTPUT FILENAME
# ============================================================

input_directory = os.path.dirname(input_file)

input_name = os.path.basename(input_file)

name_without_extension = os.path.splitext(input_name)[0]


if choice == "1":

    output_name = (
        name_without_extension
        + "_resized.jpg"
    )

elif choice == "2":

    output_name = (
        name_without_extension
        + "_compressed.jpg"
    )

elif choice == "3":

    output_name = (
        name_without_extension
        + "_resized_compressed.jpg"
    )

else:

    output_name = (
        name_without_extension
        + "_grayscale.jpg"
    )


output_file = os.path.join(
    input_directory,
    output_name
)


# ============================================================
# COMPRESSION
# ============================================================

if choice == "2" or choice == "3":

    print()
    print("--------------------------------")
    print("COMPRESSION SETTINGS")
    print("--------------------------------")


    # --------------------------------------------------------
    # GET TARGET FILE SIZE
    # --------------------------------------------------------

    while True:

        try:

            target_kb = float(
                input(
                    "Enter maximum output file size in KB: "
                )
            )

            if target_kb > 0:
                break

            print(
                "Target file size must be greater than 0."
            )

        except ValueError:

            print(
                "Please enter a number, for example 200."
            )


    target_bytes = target_kb * 1024


    # Start with high JPEG quality.
    #
    # If the resulting image is too large, progressively
    # reduce the quality until the requested file size
    # is reached.

    quality = 95

    minimum_quality = 5

    final_buffer = None
    final_size = None
    final_quality = None


    while quality >= minimum_quality:

        buffer = io.BytesIO()

        image.save(
            buffer,
            format="JPEG",
            quality=quality,
            optimize=True
        )

        current_size = buffer.tell()


        if current_size <= target_bytes:

            final_buffer = buffer

            final_size = current_size

            final_quality = quality

            break


        quality -= 5


    # --------------------------------------------------------
    # SAVE COMPRESSED IMAGE
    # --------------------------------------------------------

    if final_buffer is not None:

        with open(output_file, "wb") as file:

            file.write(
                final_buffer.getvalue()
            )


        print()
        print("--------------------------------")
        print("RESULT")
        print("--------------------------------")

        print(
            "New dimensions:",
            image.size[0],
            "x",
            image.size[1]
        )

        print(
            "Target file size:",
            target_kb,
            "KB"
        )

        print(
            "Final file size:",
            round(final_size / 1024, 2),
            "KB"
        )

        print(
            "JPEG quality used:",
            final_quality
        )

        print(
            "Saved as:",
            output_file
        )


    else:

        print()
        print("--------------------------------")
        print("TARGET COULD NOT BE REACHED")
        print("--------------------------------")

        print()

        print(
            "The image could not be reduced below",
            target_kb,
            "KB without going below the minimum",
            "JPEG quality."
        )

        print()

        print("Try one of the following:")

        print(
            "- Increase the target file size."
        )

        print(
            "- Resize the image to smaller dimensions."
        )


# ============================================================
# SAVE RESIZED OR GRAYSCALE IMAGE
# ============================================================

else:

    image.save(
        output_file,
        format="JPEG",
        quality=95,
        optimize=True
    )


    final_size = os.path.getsize(
        output_file
    ) / 1024


    print()
    print("--------------------------------")
    print("RESULT")
    print("--------------------------------")


    print(
        "New dimensions:",
        image.size[0],
        "x",
        image.size[1]
    )


    print(
        "Final file size:",
        round(final_size, 2),
        "KB"
    )


    print(
        "Saved as:",
        output_file
    )


# ============================================================
# FINISHED
# ============================================================

print()
print("Finished!")
print()
