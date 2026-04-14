import streamlit as st
from PIL import Image
import io

hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}      /* hides hamburger menu */
header {visibility: hidden;}         /* hides top header */
footer {visibility: hidden;}         /* hides "Made with Streamlit" */
</style>
"""

st.set_page_config(
    page_title="prezzlovepdf",
    page_icon="💕"
)

# MADE BY D1PREZZ DONT STEAL PLEASE?

images = []  # STORES ALL IMAGES!


st.markdown(hide_streamlit_style, unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    pass

with col2:
    st.header("prezz💗pdf")
    st.write("Convert any jpg, png, jpeg or webp to a pdf!")

with col3:
    pass


uploaded_files = st.file_uploader(
    "Upload images",
    type=["jpg", "png", "jpeg", "webp"],
    accept_multiple_files=True
)

# RESET IMAGES EVERY RUN (VERY IMPORTANT IN STREAMLIT)
images = []

if uploaded_files:
    st.write("Images uploaded!")

    for file in uploaded_files:
        img = Image.open(file)
        img = img.convert("RGB")
        images.append(img)

    for img in images:
        st.image(img, use_container_width=True)


save_button = st.button("Save")

if save_button:

    if len(images) == 0:
        st.warning("Please upload images before saving!")

    else:
        pdf_bytes = io.BytesIO()

        images[0].save(
            pdf_bytes,
            format="PDF",
            save_all=True,
            append_images=images[1:]
        )

        st.success("Images saved!")

        st.download_button(
            label="⬇Download PDF",
            data=pdf_bytes.getvalue(),
            file_name="prezz_converted.pdf",
            mime="application/pdf",
        )
