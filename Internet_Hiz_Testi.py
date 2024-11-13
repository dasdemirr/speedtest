import streamlit as st
from speedtest import Speedtest

st.title("İnternet Hız Testi")

# İnternet hız testi nesnesini oluştur
hiz_testeri = Speedtest()

if st.button("Hız Testini Başlat"):
    with st.spinner("Hız testi başlatılıyor, lütfen bekleyin..."):
        try:
            # Sunucuları listele ve en iyi sunucuyu seç
            hiz_testeri.get_servers()
            secilen_sunucu = hiz_testeri.get_best_server()
            st.write(f"Bağlanılan sunucu: {secilen_sunucu['host']} ({secilen_sunucu['country']})")

            # İndirme hızını ölç ve Mbps'e çevir
            indirme_hizi = hiz_testeri.download() / 1000000
            st.write(f"İndirme Hızı: {indirme_hizi:.2f} Mbps")

            # Yükleme hızını ölç ve Mbps'e çevir
            yukleme_hizi = hiz_testeri.upload() / 1000000
            st.write(f"Yükleme Hızı: {yukleme_hizi:.2f} Mbps")

            # Gecikme süresini (ping) al
            gecikme_suresi = hiz_testeri.results.ping
            st.write(f"Gecikme Süresi: {gecikme_suresi:.2f} ms")

        except Exception as e:
            st.error(f"Hız testi sırasında bir hata oluştu: {e}")

            #streamlit run /Users/musacan/PycharmProjects/Internet_Hiz_Testi/main.py/Internet_Hiz_Testi.py
