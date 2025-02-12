import streamlit as st

# Set page title and background color
st.set_page_config(page_title="Happy Valentine's Day", page_icon="💖", layout="centered")

# Valentine's Day message
st.title("💝 Happy Valentine's Day! 💝")
st.write("Wishing you a day filled with love and happiness! 💕")


st.markdown(
    '<img src="https://www.pinterest.com/pin/46021227434129263/" width="500">',
    unsafe_allow_html=True
)

image_url = "https://www.pinterest.com/pin/46021227434129263/"
st.image(image_url, caption="A Special Memory", use_container_width=True)

# Add interactive buttons
if st.button("💌 Click for a Special Message"):
    st.write("You are loved and appreciated! 💖 Keep smiling!")

if st.button("🎵 Play a Romantic Song"):
    st.write("Here's a beautiful song for you! 🎶 [Click Here](https://youtube.com/shorts/12XfezlwL4I?si=VNNUd6oHF3AU9Paf)")

if st.button("Click Here to celebrate This special day"):
    st.balloons()
    st.write("Hope Your life becomes More colorful as like these colors")
# if st.button("💬 Send a Virtual Hug"):
#     st.write("A big virtual hug for you! 🤗")
    
    
    # st.markdown(heart_animation, unsafe_allow_html=True)


# Footer message
st.write("---")
st.write("Made with ❤️ using Streamlit")
