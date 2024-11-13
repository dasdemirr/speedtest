Bu uygulamayı çalıştırmak için aşağıdaki Python paketlerinin yüklü olması gerekmektedir:
	•	streamlit
	•	speedtest-cli

Bu paketleri yüklemek için aşağıdaki komutu kullanabilirsiniz:

pip install streamlit speedtest-cli

Kullanım

	1.	Uygulamanın başında, kullanıcıya “İnternet Hız Testi” başlıklı bir başlık gösterilir.
	2.	Kullanıcı “Hız Testini Başlat” butonuna tıkladığında, internet hız testi başlar.
	3.	Uygulama, internet hızını ölçer ve aşağıdaki bilgileri kullanıcıya gösterir:
	4.	Bağlanılan Sunucu: Bağlantı kurulan en iyi sunucu hakkında bilgi (sunucunun adı ve ülkesi).
	5.	İndirme Hızı: İnternetten veri indirme hızınız, Mbps cinsinden.
	6.	Yükleme Hızı: İnternete veri yükleme hızınız, Mbps cinsinden.
	7.	Gecikme Süresi (Ping): Bağlantının yanıt süresi, milisaniye cinsinden.
	8.	Test sırasında bir hata oluşursa, kullanıcıya hata mesajı gösterilir.

Uygulama Kullanımı

	1.	Projeyi bilgisayarınıza indirin veya GitHub üzerinden klonlayın.
	2.	Uygulamanın ana dosyasını çalıştırmak için terminal veya komut istemcisine şu komutu yazın:
 streamlit run main.py

 Bu komut, uygulamanın yerel sunucuda çalışmasını başlatacaktır ve tarayıcı üzerinden erişilebilecektir.

Kodu Anlama

	1.	Speedtest: Speedtest kütüphanesi internet hızınızı test etmek için kullanılır. get_best_server(), download(), upload() ve ping gibi metodlarla hız ve gecikme ölçümleri yapılır.
	2.	Streamlit: streamlit kütüphanesi, basit bir arayüz oluşturmak için kullanılır. Kullanıcı arayüzü bileşenleri (st.title, st.button, st.write, vb.) ile test başlatılır ve sonuçlar ekrana yazdırılır.
Hata Yönetimi

Uygulama, herhangi bir hata durumunda kullanıcıya açıklayıcı bir hata mesajı gösterir. Bu mesajlar, bağlantı hataları veya hız testi sırasında oluşan teknik sorunları içerebilir.
