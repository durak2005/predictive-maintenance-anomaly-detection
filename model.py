"""
Kritik Sistemler ve Savunma Ekipmanları İçin Kestirimci Bakım Modeli
Yöntem: Makine Öğrenmesi (Random Forest Sınıflandırıcı) & Anomali Tespiti
"""

import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score

# 1. SENSÖR VERİSİ SİMÜLASYONU (Sıcaklık, Titreşim, Basınç, Çalışma Saati)
np.random.seed(42)
n_samples = 1000

# Normal çalışma değerleri
temperature = np.random.normal(loc=65, scale=5, size=n_samples)      # °C
vibration = np.random.normal(loc=2.5, scale=0.4, size=n_samples)     # mm/s
pressure = np.random.normal(loc=100, scale=8, size=n_samples)        # bar
operating_hours = np.random.uniform(100, 3000, size=n_samples)       # saat

# Arıza etiketi oluşturma (Fiziksel eşik kuralları bazlı simülasyon)
failure = (
    (temperature > 76) | 
    (vibration > 3.4) | 
    ((operating_hours > 2400) & (pressure < 85))
).astype(int)

# Özellik matrisi (X) ve Hedef vektör (y)
X = np.column_stack([temperature, vibration, pressure, operating_hours])
y = failure

# 2. EĞİTİM VE TEST VERİSİ AYRIMI (%80 Eğitim, %20 Test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# 3. MODEL EĞİTİMİ (Random Forest Classifier)
model = RandomForestClassifier(n_estimators=100, max_depth=5, random_state=42)
model.fit(X_train, y_train)

# 4. TAHMİN VE PERFORMANS DEĞERLENDİRME
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print("=== KESTİRİMCİ BAKIM MODELİ SONUÇLARI ===")
print(f"Model Doğruluk Oranı (Accuracy): %{accuracy * 100:.2f}\n")
print("Detaylı Sınıflandırma Raporu:")
print(classification_report(y_test, y_pred, target_names=["Normal Durum", "Arıza Riski"]))

# 5. GERÇEK ZAMANLI ERKEN UYARI TESTİ
sample_sensor_data = np.array([[78.5, 3.6, 92.0, 2500]])  # Kritik ölçüm örneği
risk_pred = model.predict(sample_sensor_data)
risk_prob = model.predict_proba(sample_sensor_data)[0][1]

print("\n=== SİMÜLE EDİLEN ERKEN UYARI ÇIKTISI ===")
print(f"Sensör Değerleri -> Sıcaklık: 78.5°C | Titreşim: 3.6 mm/s | Basınç: 92 bar")
print(f"Hesaplanan Arıza Riski: %{risk_prob * 100:.1f}")
print("Öneri / Aksiyon:", "KRİTİK UYARI: Arıza riski yüksek, bakım ekibi yönlendirilmeli!" if risk_pred[0] == 1 else "Normal Çalışma")
