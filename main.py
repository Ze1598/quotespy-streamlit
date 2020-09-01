# TODO: review tweet_graphics part
# TODO: finish graphics part
# TODO: review overall app
# TODO: deploy app

# """
# select field for module
#     if module == tweet_graphics
#         render tweet_graphics parameters
#     elif module == graphics
#         render graphics parameters
    
# button to render
# draw graphic
# """


# """graphics settings
# "font_family": "arial.ttf",
# "font_size": 250,
# "size": [2800, 2800],
# "color_scheme": ["#000000", "#ffffff"],
# "wrap_limit": 20,
# "margin_bottom": 0,
# """

from PIL import Image
import streamlit as st
import quotespy.tweet_graphics.tweet_graphics as t
import quotespy.graphics.graphics as g
from typing import Dict
st.set_option("deprecation.showfileUploaderEncoding", False)
import utils
import base64


st.markdown("""
# quotespy live demo

[quotespy](https://pypi.org/project/quotespy/) is a Python library developed by José Fernando Costa to create quotes/lyrics and tweet graphics, based on the [Pillow](https://pypi.org/project/Pillow/) library.

The library is open-source and you can find the code on [GitHub](https://github.com/Ze1598/quotespy). The code for this web app is equally available on GitHub [here]().

In this demo you're able to create graphics using both modules of quotespy: *tweet_graphics* and *graphics*. 

*tweet_graphics* lets you create graphics similar to tweet screenshots, including your username, user tag, the tweet and, optionally, a profile picture. 

*graphics* lets you create "free-form" graphics with centered text. I thought this would be most suitable for lyrics and/or quotes graphics. 

At any rate, play around with the parameters to create your ideal graphic!
""")


def render_tweet_info():
    tweet_name = st.text_input("Name for the graphic", "my_tweet")
    user_name = st.text_input("Your Twitter username", "username")
    user_tag = st.text_input("Your Twitter tag/handle", "@user")

    # Let the user upload an image for the profile picture
    user_pic = st.file_uploader(
        "Profile picture (PNG or JPG); optional", type=["png", "jpg"])
    # No profile picture defaults to empty string
    user_pic = "" if user_pic == None else user_pic
    if user_pic != "":
        # Open the profile picture and save it in the server
        img = Image.open(user_pic).save("profile_picture.png")
        user_pic = "profile_picture.png"

    tweet_text = st.text_area(
        "Your tweet (max 240 characters)", "Lorem ipsum")[:240]

    return {
        "tweet_name": tweet_name,
        "user_name": user_name,
        "user_tag": user_tag,
        "user_pic": user_pic,
        "tweet_text": tweet_text
    }


def render_tweet_graphics_params():
    font_family = st.selectbox("Font family", ("arial.ttf", "Inkfree.ttf"))
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
    transparency = float(st.slider("Background transparency", 0.0, 1.0, 1.0))
    text_color = st.beta_color_picker("Text color", "#f0f0f0")
    rgba_bg = utils.hex_to_rgba(background_color, transparency)
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


def render_graphics_params():
    st.write("graphics chosen")
    pass


module_chosen = st.selectbox("Module", ("tweet_graphics", "graphics"))

if module_chosen == "tweet_graphics":
    # Render all the parameter fields
    tweet_info = render_tweet_info()
    graphic_settings = render_tweet_graphics_params()

    st.markdown("## Result")
    # Create the graphic
    try:
        t.create_tweet(tweet_info, graphic_settings)
        # Load and display the created graphic
        graphic_name = tweet_info["tweet_name"] + ".png"
        st.write("Here's your graphic")
        st.image(graphic_name, use_column_width=True)

        # Encode the created graphic to a base64 bytes object
        encoded_img = utils.encode_img_to_b64(graphic_name)
        # Create a download link
        href = f'<a href="data:image/png;base64,{encoded_img}" download="{graphic_name}">Download the graphic</a>'
        st.markdown(href, unsafe_allow_html=True)

    except ValueError:
        st.write("There was a problem with your profile picture image. Please upload another image.")

elif module_chosen == "graphics":
    # graphic_info = render_graphic_info
    graphic_settings = render_graphics_params()


st.markdown("""
For any questions and feedback, send me an email at jose.fernando.costa.1998@gmail.com or reach out to me on Twitter @ze1598.
""")
