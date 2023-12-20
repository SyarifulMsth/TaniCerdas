import streamlit as st

st.title('TaniCerdas🌱')
st.markdown('**TaniCerdas** adalah sebuah aplikasi yang dibangun untuk memecahkan permasalahan di bidang pertanian. TaniCerdas dibangun bagi para anak muda yang ingin menjadi petani di Indonesia untuk mendeteksi penyakit pada tanaman pertanian. Tersedia juga fitur informasi penyakit yang dapat menambah pengetahuan tentang bagaimana gejala dan cara pengendalian penyakit pada tanaman pertanian. \n\n**TaniCerdas**: Petani Muda Inspiratif, Hasil Produktif!')

st.subheader('Fitur Aplikasi')

columnLeft, columnRight = st.columns(2)

with columnLeft:
    st.markdown(
        """
        Terdapat menu navigasi atau fitur di sebelahn kiri yang dapat Anda pilih sesuai kebutuhan Anda:
        - **Deteksi Tanaman Tomat** : Membantu petani mendeteksi hama atau penyakit pada daun tanaman tomat.
        - **Deteksi Tanaman Kentang** : Membantu petani mendeteksi hama atau penyakit pada daun tanaman kentang.
        - **Deteksi Tanaman Jagung** :  Membantu petani mendeteksi hama atau penyakit pada daun tanaman jagung.
        - **Informasi Penanganan** : Membantu memberikan informasi terkait hama atau penyakit pada tanaman pertanian. 
        - **Tentang Kami** : Halaman yang berisi informasi pengembang (*developer*) aplikasi TaniCerdas.
        """
    )

with columnRight:
    st.image('./images/cover_image.jpg', width=300)
    # soruce gambar
    # https://www.istockphoto.com/id/search/search-by-asset?affiliateredirect=true&assetid=1522184411&assettype=image&utm_campaign=srp_photos_bottom&utm_content=https%3A%2F%2Funsplash.com%2Fs%2Fphotos%2Ffarm-with-phone&utm_medium=affiliate&utm_source=unsplash&utm_term=farm+with+phone%3A%3A%3A
    # https://www.istockphoto.com/id/search/2/image?alloweduse=availableforalluses&mediatype=photography&phrase=farm%20with%20phone&sort=best&orientations=vertical

st.subheader("Jenis Tanaman Pertanian")
st.markdown("""Untuk saat ini TaniCerdas dapat digunakan mendeteksi penyakit untuk 3 jenis tanaman pertanian, yaitu tanaman tomat, tanaman kentang, dan tanaman jagung. Pengembangan fitur dan scala aplikasi akan dilakukan secara berkala.""")

st.markdown("""
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.0.0/dist/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
    """, unsafe_allow_html=True)

def galery():
    return """
    <div class="row">
      <!-- Gallery item -->
      <div class="col-lg-4">
        <div class="bg-white rounded shadow-sm"><img src="https://source.unsplash.com/tomato-fruits-QR1ls7DcxAs" alt="" class="img-fluid card-img-top">
          <div class="p-4">
            <h5> <a href="#" class="text-dark">Tanaman Tomat</a></h5>
          </div>
        </div>
      </div>
      <!-- End -->

      <!-- Gallery item -->
      <div class="col-lg-4">
        <div class="bg-white rounded shadow-sm"><img src="https://source.unsplash.com/green-plants-on-brown-soil-2qEv_MOltfk" alt="" class="img-fluid card-img-top">
          <div class="p-4">
            <h5> <a href="#" class="text-dark">Tanaman Kentang</a></h5>
          </div>
        </div>
      </div>
      <!-- End -->

      <!-- Gallery item -->
      <div class="col-lg-4">
        <div class="bg-white rounded shadow-sm"><img src="https://source.unsplash.com/green-corn-plant-during-daytime-qW3_HRK3ZxA" alt="" class="img-fluid card-img-top">
          <div class="p-4">
            <h5> <a href="#" class="text-dark">Tanaman Kentang</a></h5>
            </div>
          </div>
        </div>
      </div>
      <!-- End -->
    """

st.markdown(galery(),unsafe_allow_html=True)

st.divider()
st.subheader("Tanaman Tomat")
st.markdown("""Terdapat 3 jenis citra/gambar tanaman tomat yang digunakan pada aplikasi ini, yaitu penyakit hawar awal (*early blight*), penyakit daun busuk (*late blight*), dan daun tanaman sehat (*healthy*). \n\n Berikut adalah sampel dari data yang digunakan dalam membuat model *machine learning* untuk mendeteksi jenis penyakit pada tanaman tomat:""")
st.image('./images/tomat_samples.png')

st.divider()
st.subheader("Tanaman Kentang")
st.markdown("""Terdapat 3 jenis citra/gambar tanaman kentang yang digunakan pada aplikasi ini, yaitu penyakit bercak kering (*early blight*), penyakit daun busuk (*late blight*), dan daun tanaman sehat (*healthy*). \n\n Berikut adalah sampel dari data yang digunakan dalam membuat model *machine learning* untuk mendeteksi jenis penyakit pada tanaman kentang:""")
st.image('./images/kentang_samples.png')

st.divider()
st.subheader("Tanaman Jagung")
st.markdown("""Terdapat 3 jenis citra/gambar tanaman jagung yang digunakan pada aplikasi ini, yaitu penyakit hawar daun (*blight*), penyakit karat daun (*common rust*), dan daun tanaman sehat (*healthy*). \n\n Berikut adalah sampel dari data yang digunakan dalam membuat model *machine learning* untuk mendeteksi jenis penyakit pada tanaman jagung:""")
st.image('./images/jagung_samples.png')


