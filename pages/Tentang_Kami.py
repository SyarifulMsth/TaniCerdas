import streamlit as st

st.markdown("<h2 style='text-align: center; color: black;'>Creator</h2>", unsafe_allow_html=True)
st.divider()
with st.container():
    col1 = st.columns(1)[0]

    col1.write('**Nama :**    Syariful Musthofa')
    col1.write('**Pendidikan :**    Informatic Engineer Student at PGRI Semarang University')
    # col1.write('**Experience:**    8 YOE in Data Science across Banking, Fintech, and Retail')
    col1.write('**Hubungi :** [linkedin](https://www.linkedin.com/in/syariful-musthofa//) or [GitHub](https://github.com/SyarifulMsth/)')
    col1.write('**TaniCerdas** adalah sebuah aplikasi yang berbasis *Artificial Intelligence* dengan *platform* web yang hadir untuk membantu memecahkan permasalahan di bidang pertanian. Aplikasi ini dibangun menggunakan arsitektur DenseNet1212 *transfer learning* *Convolutional Neural Network* (CNN) dengan Tensorflow.')
    col1.write('**Thanks for stopping by!**')
st.divider()

st.markdown("<h2 style='text-align: center; color: black;'>Github</h2>", unsafe_allow_html=True)
st.divider()
col1, col2, col3 = st.columns(3)
col1.subheader('Nama ')
col2.subheader('Deskripsi')
col3.subheader('Github')
with st.container():
    col1, col2, col3 = st.columns(3)
    col1.write(':blue[Machine Learning Tomato Disease Detection Model]')
    col2.write('Machine learning model for detecting tomato diseases that classifies them into three classes: Early Blight, Late Blight, and Healthy.')
    col3.write('https://github.com/SyarifulMsth/TaniCerdas/blob/main/notebooks/Tomat_Models.ipynb')

with st.container():
    col1, col2, col3 = st.columns(3)
    col1.write(':blue[Machine Learning Potato Disease Detection Model]')
    col2.write('Machine learning model for detecting potato diseases that classifies them into three classes: Early Blight, Late Blight, and Healthy.')
    col3.write('https://github.com/SyarifulMsth/TaniCerdas/blob/main/notebooks/Kentang_Models.ipynb')

with st.container():
    col1, col2, col3 = st.columns(3)
    col1.write(':blue[Machine Learning Corn Disease Detection Model]')
    col2.write('Machine learning model for detecting corn diseases that classifies them into three classes: Blight, Common Rust, and Healthy.')
    col3.write('https://github.com/SyarifulMsth/TaniCerdas/blob/main/notebooks/Jagung_Models.ipynb')

with st.container():
    col1, col2, col3 = st.columns(3)
    col1.write(':blue[Deployment Code]')
    col2.write('Deployment machine learning model with Streamlit')
    col3.write('https://github.com/SyarifulMsth/TaniCerdas')

