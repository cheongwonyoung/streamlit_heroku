import streamlit as st
import cv2
from PIL import Image, ImageEnhance
import numpy as np
import os

@st.cache # 변경 사항을 감지하기 위해
def load_image(img):
    im = Image.open(img)
    return im


def main():
    """Face Detection App"""

    st.title("Face Detection App") # 글 작성
    st.text("Build with Streamlit and OpenCV") # 글 작성

    activities = ["Detection", "About"] # 선택지
    choice = st.sidebar.selectbox("Select Activity", activities) # 선택지 넣어 사이드 셀렉박스 만들기



    if choice == 'Detection': # 셀렉박스가 'Detection'일때
        st.subheader("Face Detection") # 소제목

        ### 여러 파일을 한번에 넣어 반복문을 사용하여 각 파일 단위로 행위
        # test_file = st.file_uploader("Choose a CSV file", type=['jpg', 'png','jpeg'], accept_multiple_files=True)
        #
        # for image_file in test_file:
        #     bytes_data = image_file.read()
        #
        #     st.write("filename:", image_file.name)
        #
        #     st.image(bytes_data)

        ### 단일 파일
        image_file = st.file_uploader("Upload Image", type=['jpg', 'png','jpeg']) # 세가지 종류 타입 이미지 업로드 가능

        if image_file is not None:

            our_image = Image.open(image_file)
            st.text("Original Image")
            st.image(our_image)

        enhance_type = st.sidebar.radio("Enhance Type", ["Original", "Gray-Scale","Contrast","Brightness","Blurring"])
        if enhance_type  == 'Gray-Scale':
            new_img = np.array(our_image.convert('RGB'))
            img = cv2.cvtColor(new_img,cv2.COLOR_BGR2GRAY)
            st.write(new_img)
            st.image(img)

        if enhance_type == 'Contrast':
            c_rate = st.sidebar.slider("Contrast", 0.5, 3.5 ) # 0.5 ~ 3.5 슬라이더 생성
            enhancer = ImageEnhance.Contrast(our_image) # 만들고 만들어진거에 값 적용하여 ㅇㅇ\
            img_output = enhancer.enhance(c_rate) # 바에서 설정한 값만큼 적용
            st.image(img_output)

        if enhance_type == 'Brightness':
            c_rate = st.sidebar.slider("Brightness", 0.5, 3.5 ) # 0.5 ~ 3.5 슬라이더 생성
            enhancer = ImageEnhance.Brightness(our_image) # 만들고 만들어진거에 값 적용하여 ㅇㅇ\
            img_output = enhancer.enhance(c_rate) # 바에서 설정한 값만큼 적용
            st.image(img_output)

        if enhance_type == 'Blurring':
            new_img = np.array(our_image.convert('RGB'))
            blur_rate = st.sidebar.slider("Blur", 0.5, 3.5)  # 0.5 ~ 3.5 슬라이더 생성
            blur_img = cv2.GaussianBlur(new_img,(11,11),blur_rate)
            st.image(blur_img)

        else:
            st.image(our_image, width=300)

        ### Face Detection
        task = ["Faces", "Smiles", "Eyes", "Cannize", "Cartonize"]
        feature_choice = st.sidebar.selectbox("Find Features", task) # 선택박스 생성
        if st.button("Process"): # process 버튼 생성
            if feature_choice == 'Faces':
                pass

    elif choice == 'About': # 셀렉박스가 'About'일때
        st.subheader("About") # 소제목



if __name__ == '__main__':
        main()