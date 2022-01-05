# Makine Öğrenmesi ile Canlılık Tespiti

Canlılık Tespiti

Yüz tanıma sistemlerinde görüntüdeki yüzün gerçek bir kişiye mi yoksa dijital ortamda kaydedilmiş fotoğraf veya video gibi bir kayıt mı olduğunu CNN algoritması ile
gerçek ve sahte olarak sınıflandırılarak ayırt edilmesi amaçlanmıştır.

CNN algoritması ile yapılan eğitim ve test sonuçlarını içeren bir .ipynb notebook dosyası ve bu dosyanın html kaydı klasörde paylaşılmıştır.

Projede kullanılan veri setinde doğrudan insanların fotoğraflarının kaydedildiği ve gerçek etiketinin verildiği bir dizin vardır. Aynı zamanda fotoğrafın fotoğrafı olan ve sahte olarak etiketlenmiş bir dizin daha bulunmaktadır.

Bu veri seti üzerinden MobilenetV2 ile özellik çıkarımı yapılarak CNN modeline girdi sağlanmış ve çıktı olarak 0-1 aralığında bir değer üretilmiştir. Bu değerin yüzdelik oranına göre sahte ve gerçek olma durum çıkarımı yapılmıştır. 

Sonrasında python ile hazırlanan nesne yönelimli bir program aracılığı ile opencv kütüphanesi yardımı ile kamerada yakalanan yüz çerçevesinin gerçek olup olmadığı test edilmiştir.

Makine öğrenmesi klasöründeki canlilik.py uygulaması çalıştırıldığında dahili kamera açılarak görüntü alınmakta ve bu görüntüden yüz çerçevesi yakalanmaktadır. Yüz çerçevesi yakalamak için haarcascade frontalface default olarak isimlendirilen opencv üzerinde hazır bir paket kullanılmıştır.

Python sürümü 3.6.13 olarak kullanılmıştır. Ortam olarak model eğitiminde python jupyter notebook ve nesne yönelimli program için de pycharm kullanılmıştır.
Kullanılan kütüphane sürümlerinin bilgilerinin bulunduğu bir canlilik.yaml anaconda ortam yedeği de eklenmiştir.
