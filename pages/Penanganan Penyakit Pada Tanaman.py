import streamlit as st

st.markdown("<h3 style='text-align: center; color: black;'>Informasi Penyakit atau Hama Tanaman Pertanian</h3>", unsafe_allow_html=True)
st.divider()

# TANAMAN TOMAT
st.subheader("Tanaman Tomat:tomato:")
st.markdown(
    """
    Penelitian ini mengklasifikasikan tanaman tomat ke dalam tiga kelas (<em>class</em>) berbeda, yaitu <em>Early Blight</em>, <em>Late Blight</em>, dan <em>Healthy</em>. Berikut adalah penjelasan mengenai masing-masing <em>class</em> tersebut :
    <div style="text-align: justify;">
        <ul>
            <li><strong><em>Early Blight</em></strong> (bahasa indonesia: hawar awal) merupakan penyakit yang hampir selalu ditemukan di setiap pertanian tomat. Penyebab penyakit <em>early blight</em> pada tanaman tomat adalah jamur <em>Alternaria solani</em>. Penyakit ini menyerang daun tanaman, pangkal batang hinggan buah. Gejala yang ditimbulkan penyakit ini yaitu bercak berwarna cokelat yang membentuk lingkaran konsentris yang berwarna kuning pada tanaman yang terserang. Penyakit ini dapat mengakibatkan pertumbuhan tanaman terhambat dan buah yang dihasilkan kecil serta busuk.<sup>1</sup>
            <br>Secara umum pengendalian penyakit ini adalah dengan cara menyemprot tanaman dengan fungisida secara teratur atau terjadwal. Penyemprotan dilakukan sebelum terjadinya gejela, yaitu ketika buah mulai terbentuk. Akan tetapi, seiring meningkatnya kesadaran manusia terhadap keamanan lingkungan maka penggunaan pestisida tersebut harus berdasarkan konsep PHT (Pengendalian Hama Terpadu).<sup>1</sup><sup>, 2</sup>
                <br>Terdapat 3 pendekatan yang digunakan untuk meminimalkan penggunaan pestisida berdasarkan PHT, di antaranya yaitu : 
             </li>
                <ul style="margin-left: 50px;">
                    <li>Penggunaan pestisida dapat dilakukan apabila cuaca mendukung terjadinya penyakit hawar awal; </li>
                    <li>Penggunaan pestisida dapat dilakukan apabila ambang aksi sudah tercapai. Ambang aksi merupakan tingkat populasi hama atau tingkat serangan penyakit yang memerlukan intervensi. Dengan mengukur dan memantau tingkat infestasi secara teratur, petani dapat menentukan kapan pestisida perlu diterapkan; dan </li>
                    <li>Penggunaan pestisida dapat dilakukan apabila tanaman berada pada periode kritis, yaitu saat tanaman lebih rentan terhadap serangan penyakit hawar awal. </li>
                </ul>
            <li><strong><em>Late Blight</em></strong> (bahasa indonesia: penyakit daun busuk) merupakan penyakit yang disebabkan oleh patogen Phytophthora infestans. Gejala dari penyakit penyakit ini adalah daun atau batang tanaman tampak basah, sehingga bagian tanaman tersebut berwanra menjadi coklat dan tanaman tampak seperti rusak akibat adanya embun. Salah satu cara pencegahan yang dapat dilakukan adalah dengan melakukan penyemprotan fungisida atau dengan cara teknik bottom watering, yaitu penyiraman dari bawah pot sehingga tanaman dapat terhindar dari masalah penyiraman berlebih.</li>
            <li><strong><em>Healthy</em></strong> (bahasa indonesia : sehat) mencakup tanaman tomat yang bebas dari gejala penyakit <em>early blight</em> atau Late Blight. Tanaman dalam kelas ini menunjukkan pertumbuhan dan perkembangan yang normal, tanpa tanda-tanda infeksi atau kerusakan yang signifikan. Tanaman tomat yang sehat cenderung memiliki daun yang hijau, batang yang kuat, dan buah yang berkembang dengan baik.</li>
        </ul>
    </div>
    """,
    unsafe_allow_html=True
)

# TANAMAN KENTANG
st.subheader("Tanaman Kentang:potato:")
st.markdown(
    """
    Penelitian ini mengklasifikasikan tanaman kentang ke dalam tiga kelas (<em>class</em>) berbeda, yaitu <em>early blight</em>, <em>Late Blight</em>, dan <em>Healthy</em>. Berikut adalah penjelasan mengenai masing-masing <em>class</em> tersebut :
    <div style="text-align: justify;">
        <ul>
            <li><strong><em>Early Blight</em></strong> merupakan penyakit yang disebabkan oleh jamur <em>Alternaria solani</em> yang juga menyerang tanaman kentang1. Penyakit jenis ini dapat menyebabkan bercak cokelat  tua konsentris pada daun, daun yang terinfeksi menjadi berwarna kuning mengering, hingga rontok. Sama seperti tanaman tomat, salah satu cara pencegahan penyakit <em>early blight</em> pada tanaman kentang yaitu dengan melakukan penyemprotan fungisida secara berkala.  </li>
            <li><strong><em>Late Blight</em></strong> (bahasa indonesia : hawar daun) merupakan salah satu penyakit pada tanaman kentang yang disebabkan oleh <em>Oomycetes Phytophthora infestans</em>. Penyakit jenis ini dapat mengakibatkan kerugian serius pada pertanian kentang. Gejala dari penyakit Late Blight pada tanaman kentang yaitu terdapatnya bercak luka nekrotis pada tepi daun dengan bentuk yang tidak beraturan yang berwarna gelap atau hitam kecoklatan. 
                Gejala selanjutnya yaitu bercak nekrotis pada daun akan meluas ke seluruh bagian daun dan tangkai daun. Apabila suhu lingkungan rendah dan kelembaban udara tinggi bercak nekrotis tersebut dapat menyebar di seluruh bagian tanaman kentang. Salah satu cara pencegahan yang dapat dilakukan terhadap penyakit late blight yang menyerang penyakit kentang adalah dengan melakukan penyemprotan fungisida secara berkala, tindakan yang sama seperti yang sama terhadap penyakit pada tanaman tomat.<sup>3</sup><sup>, 4</sup>
            </li>
            <li><strong><em>Healthy</em></strong> (bahasa indonesia : sehat) mencakup tanaman kentang yang tidak menunjukkan gejala penyakit <em>early blight</em> atau <em>Late Blight</em>. Tanaman dalam kelas ini tumbuh dan berkembang secara normal tanpa adanya lesi atau kerusakan yang terkait dengan penyakit.</li>
        </ul>
    </div>
    """,
    unsafe_allow_html=True
)

# TANAMAN JAGUNG
st.subheader("Tanaman Jagung:corn:")
st.markdown(
    """
    Penelitian ini mengklasifikasikan tanaman jagung ke dalam tiga kelas (<em>class</em>) berbeda, yaitu <em>Blight</em>, <em>Common Rust</em>, dan <em>Healthy</em>. Berikut adalah penjelasan mengenai masing-masing <em>class</em> tersebut :
    <div style="text-align: justify;">
        <ul>
            <li><strong><em>Blight</em></strong> atau <em>corn leaf blight</em> (bahasa indonesia : hawar daun) adalah salah satu jenis penyakit yang menyerang tanaman jagung yang disebabkan oleh jamur <em>Setosphaeria turcica</em>. Gejala yang timbul dari penyakit jenis ini yaitu timbulnya bercak-bercak kecil, lonjong, basah, pada bagian bawah terlebih dahulu. Gejala berikutnya bercak-bercak tersebut mulai muncul di bagian atas tanaman. Bercak-bercak yang lebih tua perlahan-lahan akan tumbuh menjadi lesi (kerusakan) cokelat nekrotik berbentuk cerutu panjang. Apabila gejala tersebut menyebar ke sebagian besar atau daun tanaman, maka dapat menyebabkan kematian pada tanaman. Pengendalian atau pencegahan penyakit jenis ini dapat dilakukan dengan cara pengendalian kimiawi atau pengendalian hayati, seperti penggunaan fungisida secara tepat.</li>
            <li><strong><em>Common Rust</em></strong> (bahasa indonesia : karat daun jagung) adalah penyakit pada tanaman jagung yang disebabkan oleh jamur <em> Puccinia sorghi</em>. Gejala awal dari penyakit ini berupa bintik klorosis pada daun, atau terdapat benjolan berwarna coklat keemasan pada permukaan daun tanaman jagung. Penyebaran penyakit karat ini sangat mudah sekali. Ukuran spora yang kecil dengan jumlah yang sangat banyak mengakibatkan patogen mudah berpindah ke tanaman lainnya yang sehat. Spora tersebut dapat tertiup angin dan menginfeksi tanaman lainnya. Serangan penyakit ini menyebabkan proses fotosintesis terganggu sehingga pertumbuhan tanaman menjadi terhambat dan tanaman menjadi kerdil. Hal tersebut dapat berimplikasi terhadap tingkat produksi pertanian yang menurun.<sup>5</sup> 
            <br>Secara umum, terdapat beberapa cara untuk pengendalian penyakit ini pada tanaman jagung, di antaranya yaitu menanam varietas yang tahan terhadap penyakit jenis ini, mengatur jarak antar tanaman agar suhu dan kelembapan tanaman dapat terjaga, melakukan penanaman yang tepat secara serempak, yaitu menanam di awal musim kemarau, dan apabila intensitas serangan penyakit cukup tinggi maka dapat menggunakan pestisida dengan dosis yang telah ditentukan.  </li>
            <li><strong><em>Healthy</em></strong> (bahasa indonesia : sehat) mencakup tanaman jagung yang tidak terinfeksi oleh penyakit <em>blight</em> atau <em>common rust</em>. Tanaman dalam kelas ini menunjukkan pertumbuhan yang normal, daun yang berwarna hijau, dan tidak ada gejala penyakit yang tampak. Pengelolaan pertanian yang baik, termasuk penggunaan varietas tahan penyakit dan praktik budidaya yang tepat, dapat membantu menjaga kesehatan tanaman jagung dan meningkatkan hasil pertanian secara keseluruhan.</li>
        </ul>
    </div>
    """,
    unsafe_allow_html=True
)

# Referensi
st.subheader("Daftar Referensi")
st.markdown("""
    <div style="text-align: justify;">
        <p><span style="display: inline-block; text-indent: -1.5em; margin-left: 2em;">[1] E. P. I. Nuviani, M. Martosudiro, and F. A. Choliq, “Pengaruh Beberapa Fungisida Terhadap Alternaria solani Penyebab Penyakit Bercak Kering Pada Tanaman Tomat (Lycopersicum esculentum Mill.) Di Lapangan,” J. Hama dan Penyakit Tumbuh., vol. 11, no. 2, pp. 84–92, 2023, doi: 10.21776/ub.jurnalhpt.2023.011.2.4.</span></p>
        <p><span style="display: inline-block; text-indent: -1.5em; margin-left: 2em;">[2] Haverkort, A. J.; Struik, P. C.; Visser, R. G. F.; Jacobsen, E (2009), "Applied biotechnology to combat late blight in potato caused by Phytophthora infestans", Potato Research (Submitted manuscript), 52 (3): 249–64, doi:10.1007/s11540-009-9136-3, S2CID 2850128</span></p>
        <p><span style="display: inline-block; text-indent: -1.5em; margin-left: 2em;">[3] S. Purwantisari, A. Priyatmojo, R. P. Sancayaningsih, and R. S. Kasiamdari, “Masa Inkubasi Gejala Penyakit Hawar Daun Tanaman Kentang yang Diinduksi Ketahanannya oleh Jamur Antagonis Trichoderma viride,” Bioma Berk. Ilm. Biol., vol. 18, no. 2, p. 41, 2016, doi: 10.14710/bioma.18.2.41-47.</span></p>
        <p><span style="display: inline-block; text-indent: -1.5em; margin-left: 2em;">[4] S. Purwantisari, R. S. Ferniah, and B. Raharjo, “Pengendalian Hayati Penyakit Hawar Daun Tanaman Kentang Dengan Agens Hayati Jamur-jamur Antagonis Isolat Lokal,” BIOMA J. Biol. MAKASSAR - J. Unhas, vol. 10, no. 2, pp. 51–57, 2008.</span></p>
        <p><span style="display: inline-block; text-indent: -1.5em; margin-left: 2em;">[5] R. Ruimassa, E. A. Martanto, D. K. Erari, and A. Yaku, “Ketahanan beberapa varietas jagung (Zea mays L.) terhadap penyakit karat daun (Puccinia sorghi) di Dusun Copti Distrik Prafi Kabupaten Manokwari,” Agrotek, vol. 10, no. 1, pp. 19–26, 2022, doi: 10.46549/agrotek.v10i1.240.</span></p>
    </div>
""", unsafe_allow_html=True)
