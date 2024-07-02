# import streamlit as st
# import cv2
# from PIL import Image
# import numpy as np

# st.title("Image Parser")

# # Create a file uploader widget
# uploaded_file = st.file_uploader("Select an image", type=["jpg", "jpeg", "png"])

# if uploaded_file is not None:
#     # Read the uploaded image using OpenCV
#     img_bytes = uploaded_file.read()
#     img = cv2.imdecode(np.frombuffer(img_bytes, np.uint8), cv2.IMREAD_COLOR)

#     # Display the original image
#     st.image(img)

#     # Create a button to parse the image
#     if st.button("Parse Image"):
#         # Perform some image processing or parsing logic here (e.g. edge detection, thresholding, etc.)
#         # For this example, let's just convert the image to grayscale
#         gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#         st.image(gray)

#     # Create a text area to display any output from the image processing
#     output_text = ""
#     if st.button("Get Text"):
#         # Perform some OCR logic here (e.g. using Tesseract-OCR or OpenCV's built-in OCR)
#         # For this example, let's just return a fake output string
#         output_text = "This is some fake text output"
#         st.text_area("Output:", value=output_text)

from ollama import Client

client = Client(host='http://192.168.0.107:11435')

response = client.chat(model='llama3:8b', messages=[{
    "role":"user",
    "content":"Do you think Dallas could win G1 today against Celtics?"
}])

print(response['message']['content'])

# conda create --name clinmatch_streamlit --clone clinmatch

