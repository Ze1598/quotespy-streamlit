import streamlit as st
import base64
from PIL import Image
from io import BytesIO
from typing import Dict
import quotespy.tweet_graphics.tweet_graphics as t
import quotespy.graphics.graphics as g
import os


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


def validate_user_tag(user_tag: str) -> str:
    """Validate user tag with the @ character at the beginning.
    """
    if not user_tag.startswith("@"):
        user_tag = "@" + user_tag[:15]
    else:
        user_tag = user_tag[:15]

    return user_tag


def save_profile_picture(path: str) -> None:
    """Save the uploaded profile picture if one was uploaded.
    """
    if path != "":
        # Open the profile picture and save it in the server
        img = Image.open(path).save("profile_picture.png")
        user_pic = "profile_picture.png"


def render_tweet_info() -> Dict:
    """Render all the input fields for the tweet_graphics graphics.
    """
    tweet_name = st.text_input("Name for the graphic", "my_tweet")
    user_name = st.text_input(
        "Your Twitter username (max 50 characters)", "username")[:50]

    user_tag = st.text_input(
        "Your Twitter tag/handle (max 15 characters)", "@user")
    user_tag = validate_user_tag(user_tag)

    # Let the user upload an image for the profile picture
    user_pic = st.file_uploader(
        "Profile picture (PNG or JPG); optional", type=["png", "jpg"])
    # No profile picture defaults to empty string
    user_pic = "" if user_pic == None else user_pic
    # Save the profile picture so it can be used in the graphic (an\
    # empty string will do nothing)
    save_profile_picture(user_pic)

    tweet_text = st.text_area(
        "Your tweet (max 240 characters)", "Lorem ipsum")[:240]

    return {
        "tweet_name": tweet_name,
        "user_name": user_name,
        "user_tag": user_tag,
        "user_pic": user_pic,
        "tweet_text": tweet_text
    }


def choose_font(input_font: str) -> str:
    """Given the font chosen by the user in the input field, return the path to the .ttf file.
    """
    if input_font == "Arial":
        font_path = os.path.join("static", "fonts", "arial.ttf")
    elif input_font == "Inkfree":
        font_path = os.path.join("static", "fonts", "Inkfree.ttf")
    else:
        font_path = os.path.join("static", "fonts", "arial.ttf")

    return font_path


def render_tweet_graphics_params() -> Dict:
    font_family_input = st.selectbox("Font family", ("Arial",))
    # Get the path to the font chosen by the user
    font_family = choose_font(font_family_input)

    font_size_header = int(st.text_input("Font size (header)", "80"))
    font_size_text = int(st.text_input("Font size (text)", "100"))
    graphic_width = int(st.text_input("Graphic width (pixels)", "1800"))
    graphic_height = int(st.text_input("Graphic height (pixels)", "1800"))
    size = [graphic_width, graphic_height]

    st.write(
        "You can ignore the profile picture dimensions if you won't include a profile picture")
    prof_pic_width = int(st.text_input(
        "Profile picture width for the graphic (pixels)", "0"))
    prof_pic_height = int(st.text_input(
        "Profile picture height for the graphic (pixels)", "0"))
    profile_pic_size = [prof_pic_width, prof_pic_height]

    background_color = st.beta_color_picker("Background color", "#000000")
    transparency = float(st.slider(
        "Background transparency (0 is completely transparent // 1 is completely opaque)", 0.0, 1.0, 1.0))
    text_color = st.beta_color_picker("Text color", "#f0f0f0")
    rgba_bg = hex_to_rgba(background_color, transparency)
    color_scheme = [rgba_bg, text_color]

    wrap_limit = int(st.text_input(
        "Maximum number of characters per line", "32"))
    margin_bottom = int(st.text_input(
        "Vertical margin between lines of text (pixels)", "32"))

    return {
        "font_family": font_family,
        "font_size_text": font_size_text,
        "font_size_header": font_size_header,
        "size": size,
        "profile_pic_size": profile_pic_size,
        "color_scheme": color_scheme,
        "wrap_limit": wrap_limit,
        "margin_bottom": margin_bottom
    }


def render_graphic_info() -> Dict:
    graphic_name = st.text_input("Name for the graphic", "my_graphic")
    graphic_text = st.text_area("Text to draw in the graphic", "Lorem ipsum")

    return {
        "title": graphic_name,
        "text": graphic_text
    }


def render_graphics_params() -> Dict:
    font_family_input = st.selectbox(
        "Font family", ("Arial", "Inkfree"))
    # Get the path to the font chosen by the user
    font_family = choose_font(font_family_input)
    font_size_header = int(st.text_input("Font size", "250"))
    graphic_width = int(st.text_input("Graphic width (pixels)", "1920"))
    graphic_height = int(st.text_input("Graphic height (pixels)", "1080"))
    size = [graphic_width, graphic_height]

    background_color = st.beta_color_picker("Background color", "#060F56")
    transparency = float(st.slider(
        "Background transparency (0 is completely transparent // 1 is completely opaque)", 0.0, 1.0, 1.0))
    text_color = st.beta_color_picker("Text color", "#D4BF2D")
    rgba_bg = hex_to_rgba(background_color, transparency)
    color_scheme = [rgba_bg, text_color]

    wrap_limit = int(st.text_input(
        "Maximum number of characters per line", "32"))
    margin_bottom = int(st.text_input(
        "Vertical margin between lines of text (pixels)", "32"))

    return {
        "font_family": font_family,
        "font_size": font_size_header,
        "size": size,
        "color_scheme": color_scheme,
        "wrap_limit": wrap_limit,
        "margin_bottom": margin_bottom
    }


def create_graphic(module: str, info: Dict, g_settings: Dict) -> str:

    if module == "t":
        try:
            t.create_tweet(info, g_settings)
            # Load and display the created graphic
            graphic_name = info["tweet_name"] + ".png"

        except ValueError:
            st.write(
                "There was a problem with your profile picture image. Please upload another image.")

    elif module == "g":
        try:
            g.create_graphic(info, g_settings)
            # Load and display the created graphic
            graphic_name = info["title"] + ".png"

        except ValueError:
            st.write(
                "There was a problem with your profile picture image. Please upload another image.")

    return graphic_name
