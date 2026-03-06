import streamlit as st

# Sahifa sozlamalari
st.set_page_config(
    page_title="AI Vision Pro — YOLOv8 Obyekt Aniqlash",
    page_icon="🔍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS (dizayn uchun)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

    * {
        font-family: 'Inter', sans-serif;
    }

    .main {
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
        color: #e2e8f0;
    }

    .hero {
        background: linear-gradient(rgba(99, 102, 241, 0.75), rgba(139, 92, 246, 0.75)), 
                    url('https://thumbs.dreamstime.com/b/abstract-digital-network-background-glowing-connected-dots-lines-generative-ai-dynamic-depicting-interconnected-435384026.jpg') center/cover no-repeat;
        background-blend-mode: multiply;  /* rasm ustiga gradient qoraytirish uchun */
        border-radius: 20px;
        padding: 6rem 2rem;
        text-align: center;
        margin: -1rem -4rem 3rem -4rem;
        box-shadow: 0 15px 50px rgba(99,102,241,0.4);
        min-height: 500px;  /* rasm to'liq ko'rinishi uchun balandlik */
        display: flex;
        flex-direction: column;
        justify-content: center;
        color: white;
        position: relative;
    }

    .hero h1 {
        font-size: 4.2rem;
        margin-bottom: 0.8rem;
        color: white;
    }

    .hero p {
        font-size: 1.4rem;
        opacity: 0.95;
        max-width: 800px;
        margin: 0 auto 2rem;
        color: #f1f5f9;
    }

    .feature-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(340px, 1fr));
        gap: 2rem;
        margin: 3rem 0;
    }

    .feature-card {
        background: rgba(30,41,59,0.75);
        border: 1px solid rgba(139,92,246,0.3);
        border-radius: 16px;
        overflow: hidden;
        transition: all 0.35s ease;
        text-align: center;
    }

    .feature-card:hover {
        transform: translateY(-12px);
        box-shadow: 0 20px 50px rgba(139,92,246,0.35);
        border-color: #c084fc;
    }

    .feature-img {
        width: 100%;
        height: 220px;
        object-fit: cover;
        border-bottom: 4px solid #8b5cf6;
    }

    .feature-content {
        padding: 1.6rem 1.2rem;
    }

    .feature-title {
        color: #c4b5fd;
        font-size: 1.5rem;
        margin-bottom: 0.8rem;
    }

    .feature-desc {
        color: #cbd5e1;
        font-size: 1rem;
        line-height: 1.6;
    }

    

    section[data-testid="stSidebar"] {
    background: linear-gradient(180deg,#0f172a,#1e293b) !important;
    border-right: 1px solid rgba(139,92,246,0.3);
    }
    
    section[data-testid="stSidebar"] * {
        color: #e2e8f0 !important;
    }
    
    .sidebar-card {
        background: rgba(255,255,255,0.05);
        border-radius: 12px;
        padding: 1rem;
        margin-bottom: 1rem;
        border: 1px solid rgba(139,92,246,0.25);
    }
    
    .sidebar-card:hover{
        border-color:#c084fc;
        transform:translateY(-2px);
        transition:0.3s;
    }
    
    .sidebar-title{
        font-size:1.4rem;
        font-weight:600;
        color:#c4b5fd;
        text-align:center;
        margin-bottom:1rem;
    }
    </style>
""", unsafe_allow_html=True)



# Hero qismi
st.markdown("""
    <div class="hero">
        <h1>AI Vision Pro</h1>
        <p>YOLOv8 asosida real vaqtda obyektlarni aniqlash — kamera, rasm va video uchun kuchli platforma</p>
    </div>
""", unsafe_allow_html=True)

# Kirish matni
st.markdown("""
    <h2 style="text-align:center; color:#c4b5fd; margin:2rem 0 1rem;">Nima uchun bizning tizim?</h2>
    <p style="text-align:center; max-width:900px; margin:0 auto 3rem; color:#cbd5e1; font-size:1.1rem;">
        Tez, aniq va foydalanish oson. 80+ turdagi obyektlarni (odam, mashina, hayvon, buyum va boshqalar) 
        soniyada 30+ kadr tezligida aniqlaydi. Xavfsizlik, monitoring, transport tahlili yoki shaxsiy loyihalar uchun ideal.
    </p>
""", unsafe_allow_html=True)


st.html("""
    <div style="display: flex; justify-content: center; flex-wrap: wrap; gap: 3rem; margin: 3rem 0 4rem;">

        <div style="text-align: center; max-width: 220px;">
            <div style="font-size: 100px; color: #a78bfa; margin-bottom: 1rem;">⚡</div>
            <h3 style="color: #c4b5fd; font-size: 1.4rem; margin-bottom: 0.5rem;">Yuqori Tezlik</h3>
            <p style="color: #cbd5e1; font-size: 1rem;">
                Soniyada 30+ kadr tezligida ishlash. YOLOv8 nano modeli bilan real vaqtda monitoring.
            </p>
        </div>

        <div style="text-align: center; max-width: 220px;">
            <div style="font-size: 100px; color: #a78bfa; margin-bottom: 1rem;">🎯</div>
            <h3 style="color: #c4b5fd; font-size: 1.4rem; margin-bottom: 0.5rem;">Yuqori Aniqlik</h3>
            <p style="color: #cbd5e1; font-size: 1rem;">
                80+ turdagi obyektlarni yuqori confidence bilan aniqlaydi. Kam xato va ishonchli natijalar.
            </p>
        </div>

        <div style="text-align: center; max-width: 220px;">
            <div style="font-size: 100px; color: #a78bfa; margin-bottom: 1rem;">🖱️</div>
            <h3 style="color: #c4b5fd; font-size: 1.4rem; margin-bottom: 0.5rem;">Qulay Foydalanish</h3>
            <p style="color: #cbd5e1; font-size: 1rem;">
                Intuitiv interfeys, oddiy sozlamalar va real vaqtda natijalarni ko'rish — tajribasiz foydalanuvchilar uchun ham oson.
            </p>
        </div>

        

    </div>
""")


st.markdown('<h2 style="text-align:center; color:#a78bfa; margin:3rem 0 2rem;">✨ Asosiy Imkoniyatlar</h2>', unsafe_allow_html=True)

st.html("""
<div class="feature-grid">

    <div class="feature-card">
        <img src="https://cdn.prod.website-files.com/62fba5686b6d47653f1ed2ae/66c4d0ca3a917b5c2502fb4a_AD_4nXfCYzB3nPwjzRnkzgLicsMCVSeBGsRpJjXofXVz01UMCv_1pVbeiuIM05INc93CuX9xY6RB_1BIXsVxpImxA0A2LUBvjzX3e279rTwz3DIQrFFw7aBVnq9KFSi8h89fnGkh58j77GunNinYR5cg75_Z23tJ.png" 
             alt="Real-time Kamera" class="feature-img">
        <div class="feature-content">
            <div class="feature-title"> Real-time Kamera Aniqlash</div>
            <p class="feature-desc">
                Kompyuter yoki telefon kamerasi orqali jonli video strimda obyektlarni aniqlaydi. 
                Har bir kadrda bounding box'lar chiziladi, obyekt turlari va soni real vaqtda hisoblanadi. 
                FPS ko'rsatkichini kuzatib, yuqori tezlikda monitoring qilish mumkin — xavfsizlik kameralari, do'kon tahlili uchun juda qulay.
            </p>
        </div>
    </div>

    <div class="feature-card">
        <img src="https://keylabs.ai/blog/content/images/2024/01/kl-8.jpg" 
             alt="Rasm Tahlili" class="feature-img">
        <div class="feature-content">
            <div class="feature-title"> Rasm Yuklash va Tahlil</div>
            <p class="feature-desc">
                JPG, PNG yoki boshqa formatdagi rasmlarni yuklang va bir zumda natijani ko'ring. 
                Aniqlangan obyektlarga bounding box chiziladi, natijani saqlab olish yoki yuklab olish mumkin. 
                Tez va oddiy — bir necha soniyada professional tahlil olasiz.
            </p>
        </div>
    </div>

    <div class="feature-card">
        <img src="https://cdn.prod.website-files.com/62fba5686b6d47653f1ed2ae/66ba4dd3b1dcc06c0107ddbf_AD_4nXdX13QEoZESHyxwjFGiIxiNkbBQHHur0PuG5DTdOjieDAYBew8RKc6l4nOymVoBSCXP3VL_Ul2bUHTiyHGESwY1LNL1y9HPtq-Okazo6ljxBVoJ6HprKHxYw_OBuHOwB0NoAOl4F-Jy3n7K4xSjNHEohmnn.png" 
             alt="Video Tahlili" class="feature-img">
        <div class="feature-content">
            <div class="feature-title"> Video Fayl Tahlili</div>
            <p class="feature-desc">
                MP4 yoki boshqa video formatlarni yuklang — tizim har bir kadrni avtomatik tahlil qiladi. 
                Harakatdagi obyektlarni aniqlash, sonini hisoblash va statistika chiqarish imkoniyati mavjud. 
                Video monitoring yoki post-processing uchun ajoyib yechim.
            </p>
        </div>
    </div>

    <div class="feature-card">
        <img src="https://learnopencv.com/wp-content/uploads/2022/11/yolov5-v6-v7-fps-performance-comparison-640-rtx4090-sorted-1024x601.png" 
             alt="Statistika Dashboard" class="feature-img">
        <div class="feature-content">
            <div class="feature-title"> Statistika va Vizualizatsiya</div>
            <p class="feature-desc">
                Aniqlangan obyektlar soni, FPS (kadr/sekund), confidence darajasi va grafik ko'rinishdagi natijalar. 
                Real vaqtda dashboard orqali kuzatish mumkin. 
                Ma'lumotlarni tahlil qilish va hisobot tayyorlash uchun juda qulay.
            </p>
        </div>
    </div>

</div>
""")

# Call to Action
st.markdown("""
<style>
    div.stButton > button {
        background: linear-gradient(90deg, #a78bfa, #c084fc) !important;
        color: white !important;
        padding: 1rem 3rem !important;
        font-size: 1.3rem !important;
        font-weight: bold !important;
        border: none !important;
        border-radius: 999px !important;
        box-shadow: 0 10px 30px rgba(168,85,247,0.4) !important;
        transition: all 0.4s ease !important;
        min-width: 320px !important;
    }

    div.stButton > button:hover {
        transform: translateY(-4px) !important;
        box-shadow: 0 15px 45px rgba(168,85,247,0.6) !important;
    }

    div.stButton > button:active {
        transform: translateY(-2px) !important;
    }
</style>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1,2,1])
with col2:
    if st.button("Tizimni sinab ko'rish →", key="big_cta"):
        st.switch_page("pages/🔎_Obyektni_aniqlash.py")


with st.sidebar:

    st.logo(
        image="https://cdn-icons-png.flaticon.com/512/4712/4712035.png",
        # image='🤖',
        size='large'
    )


    st.markdown("<div class='sidebar-title'>AI Vision Pro</div>", unsafe_allow_html=True)

    st.markdown("""
    <div class="sidebar-card">
    <b>Versiya</b><br>
    1.0 — 2026
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="sidebar-card">
    <b>Model</b><br>
    YOLOv8n optimallashtirilgan model
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="sidebar-card">
    <b>Tavsiyalar</b><br>
    • Aniqlashda yorug'lik yaxshi bo'lsin<br>
    • Confidence: 0.35 – 0.60 oralig'ida<br>
    • Real time aniqlashda internet sifati tasir qiladi
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="sidebar-card">
    <b>🔗 Havolalar</b><br>
    <a href="https://docs.ultralytics.com/models/yolov8/" target="_blank">YOLOv8 Docs</a><br>
    <a href="https://github.com/ultralytics/ultralytics" target="_blank">Ultralytics GitHub</a><br>
    <a href="https://opencv.org/" target="_blank">OpenCV</a>
    </div>
    """, unsafe_allow_html=True)

    st.caption("©2026 TATU")

# Pastki qism (footer)
st.markdown("---")
st.markdown("""
    <div style='text-align:center; color:#94a3b8; padding:2rem 0;'>
        AI Vision Pro — YOLOv8 + Streamlit loyihasi<br>
        Tez, aniq va oson foydalaniladigan obyekt aniqlash tizimi
    </div>
""", unsafe_allow_html=True)