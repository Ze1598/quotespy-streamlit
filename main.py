import base64
import utils
from PIL import Image
import streamlit as st
st.set_option("deprecation.showfileUploaderEncoding", False)

st.markdown("""
# quotespy live demo

[quotespy](https://pypi.org/project/quotespy/) is a Python library developed by José Fernando Costa to create quotes/lyrics and tweet graphics, based on the [Pillow](https://pypi.org/project/Pillow/) library.

The library is open-source and you can find the code on [GitHub](https://github.com/Ze1598/quotespy). The code for this web app is equally available on GitHub [here]().

In this demo you're able to create graphics using both modules of quotespy: *tweet_graphics* and *graphics*. 

*tweet_graphics* lets you create graphics similar to tweet screenshots, including your username, user tag, the tweet and, optionally, a profile picture. 

*graphics* lets you create "free-form" graphics with centered text. I thought this would be most suitable for lyrics and/or quotes graphics. 

At any rate, play around with the parameters to create your ideal graphic!

For any questions and feedback, send me an email at jose.fernando.costa.1998@gmail.com or reach out to me on Twitter @ze1598.
""")

# Choose which type of graphic to create, that is, choose the quotespy module
module_chosen = st.selectbox("Module", ("tweet_graphics", "graphics"))

# Render the input fields for each module and create the resulting graphic
# ---------------------------------------------------------
if module_chosen == "tweet_graphics":
    tweet_info = utils.render_tweet_info()
    graphic_settings = utils.render_tweet_graphics_params()
    graphic_name = utils.create_graphic("t", tweet_info, graphic_settings)

elif module_chosen == "graphics":
    graphic_info = utils.render_graphic_info()
    graphic_settings = utils.render_graphics_params()
    graphic_name = utils.create_graphic("g", graphic_info, graphic_settings)


# Display the resulting graphic
# ---------------------------------------------------------
st.markdown("## Resulting graphic")
st.image(graphic_name, use_column_width=True)

# Create a download link for the graphic by encoding the file to b64 bytes object
# ---------------------------------------------------------
encoded_img = utils.encode_img_to_b64(graphic_name)
href = f'<a href="data:image/png;base64,{encoded_img}" download="{graphic_name}">Download the graphic</a>'
st.markdown(href, unsafe_allow_html=True)
