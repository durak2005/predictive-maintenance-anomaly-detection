# Savunma ve Üretim Sistemlerinde Kestirimci Bakım ve Anomali Tespiti (Predictive Maintenance)

Bu proje; kritik mekanik sistemler, güç aktarım üniteleri ve savunma platformlarının telemetri sensör verilerini (sıcaklık, titreşim, basınç, çalışma saati) sürekli analiz ederek arızaları oluşmadan önce öngören bir **Makine Öğrenmesi Tabanlı Erken Uyarı Sistemidir**.

---

## 🎯 Problem Tanımı ve Mühendislik Yaklaşımı
Plansız duruşlar (unplanned downtime) üretim hatlarında yüksek maliyet kaybına, savunma platformlarında ise operasyonel risklere yol açar.
* **Yaklaşım:** Geleneksel periyodik bakım yerine, sensör verilerine dayalı dinamik kestirimci bakım (Predictive Maintenance).
* **Yöntem:** Çok değişkenli sensör anomali eşiklerinin modellenmesi ve `Random Forest` algoritması ile arıza olasılıklarının gerçek zamanlı sınıflandırılması.

---

## 🛠️ Kullanılan Teknolojiler ve Kütüphaneler
* **Dil:** Python 3
* **Makine Öğrenmesi & Veri Analitiği:** `scikit-learn`, `numpy`
* **Metotlar:** Sınıflandırma Analizi, Özellik Mühendisliği (Feature Engineering), Güvenilirlik Analitiği

---

## 📊 Model Çıktıları ve Performans Metrikleri
* Test verisi üzerinde **%94+ sınıflandırma doğruluğu (Accuracy)**.
* Kritik arıza modlarında yüksek yakalama oranı (Recall & F1-Score).
* Bakım maliyetlerinde ve arıza kaynaklı operasyonel duruşlarda önleyici tasarruf potansiyeli.

---

## 👥 Proje Ekibi ve Görev Dağılımı
* **Aşkın Durak (@durak2005):** Sensör Veri Mimarisi, Özellik Mühendisliği (Feature Engineering) & Model Eğitimi
* **Hasan Curtay (@Hasancrty):** Anomali Eşik Analizi, Model Hiperparametre Optimizasyonu & Test Senaryoları
* **Gözdenur Kaya (@imgozdeky-spec):** Model Doğrulama, Performans Metrikleri & Dokümantasyon
