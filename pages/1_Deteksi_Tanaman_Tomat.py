import streamlit as st
from keras.models import load_model
from PIL import Image

from util import classify, set_background

# set_background('./images/petani.jpg')

# Set titlecs
st.markdown("<h3 style='text-align: center; color: black;'>Deteksi Penyakit atau Hama Tanaman Tomat</h3>", unsafe_allow_html=True)

# upload File
uploaded_file = st.file_uploader('**Catatan** : Mohon untuk unggah gambar daun tanaman Tomat! Kesalahan unggah gambar dapat mengakibatkan prediksi yang tidak akurat.', type=['jpeg', 'jpg', 'png'])

# load classifier
model = load_model('./models/models_tomat.h5')

# load class names
with open('./models/labels_tomat.txt', 'r') as f:
    class_names = [a[:-1].split(' ')[1] for a in f.readlines()]
    f.close()

print(class_names)

# display image
if uploaded_file is not None:
    image = Image.open(uploaded_file).convert('RGB')
    # st.image(image, use_column_width=True)
    st.image(image, width=180, caption="Gambar telah berhasil diunggah!")

    # classify image
    class_name, conf_score = classify(image, model, class_names)

    # write classification
    st.write("### Class : {}".format(class_name))
    st.write("### Accuracy : {}".format(conf_score))
    # st.write("## {}".format(class_name))
    # st.write("### Score : {}".format(conf_score))

else:
    st.write("Tidak ada gambar yang diunggah.")
