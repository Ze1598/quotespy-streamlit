import base64
from PIL import Image
from io import BytesIO


def hex_to_rgba(hex_color: str, alpha: float) -> str:
    """Given a hexadecimal color string and a transparency in the 0-1 range, convert it to a rgba color string.
    """
    # Convert the hex color to a rbg tuple
    # Take each pair of two digits in the hex color and convert them from\
    # base 16 to base 10; save each pair as a RGB channel in a tuple
    # https://stackoverflow.com/a/29643643/9263761
    hex_to_rgb = tuple(int(hex_color[i:i+2], 16) for i in (1, 3, 5))

    # Add a fourth channel to simulate the transparency in a rgba color
    rgba_tuple = hex_to_rgb + (alpha,)

    # Store the rgba color as a string
    rgba_bg = f"rgba{rgba_tuple}"

    return rgba_bg


def encode_img_to_b64(img_name: str) -> bytes:
    """Given the name of a image file, load it in bytes mode, and convert it to a base 64 bytes object.
    """
    with open(img_name, "rb") as f:
        img = f.read()
        encoded_img = base64.b64encode(img).decode()

    return encoded_img
    # img = Image.open(img_name)
    # buffered = BytesIO()
    # img.save()
