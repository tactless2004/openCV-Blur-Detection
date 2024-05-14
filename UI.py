import streamlit as st
import cv2
from ComputeLaplacian import variance_of_laplacian
st.title(":ocean: Blur Detection")
images = st.file_uploader(label="Upload Image",accept_multiple_files=True,type=['jpg','png','jpeg','tiff','.webp'])
threshold_str = st.text_input("Threshold for the Laplacian", value="100")
threshold = None
try:
    threshold = float(threshold_str)
    if(threshold < 0):
        st.markdown(":red[Threshold must be a positively valued float]")
        threshold=None
except:
    st.markdown(":red[Threshold must be a float]")

"---"
output_images = []
index = 1

for image in images:
    if image is not None and threshold is not None:
        st.header("Image {index}".format(index=index))
        st.image(image)
        src = cv2.imread(image.name)
        image_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
        var = variance_of_laplacian(image_gray)
        st.header(":dart: Analysis")
        if(var > threshold):
            st.markdown(":blue[Not Blurry: {var:.2f}]".format(var=var))
            output_images.append(image)
        else:
            st.markdown(":red[Blurry: {var:.2f}]".format(var=var))
        index += 1
        "---"
