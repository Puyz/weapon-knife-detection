[🇹🇷 Türkçe](#tr) | [🇬🇧 English](#en)

<a id="tr"></a>

# VİDEODA VEYA KAMERADA BIÇAK VE ATEŞLİ SİLAH TESPİTİ

## PROBLEM TANIMI
- Güvenlik alanlarında, özellikle kamu yerlerinde, bıçak ve ateşli silahların tespiti hayati önem taşımaktadır. Günümüzde, bu tür tehlikeli nesnelerin tespit edilmesi için etkili ve hızlı yöntemlere ihtiyaç duyulmaktadır. Bu proje, video dosyaları veya canlı kamera akışlarında gerçek zamanlı olarak bıçak ve ateşli silah tespiti yapmayı amaçlar.

## PROBLEMİN ÇÖZÜMÜ
- Problemin çözümü için YOLOv8 modeli kullanılarak tespit gerçekleştirilmiştir. Bu model, Roboflow ile etiketlenmiş veriler üzerinde eğitilmiş ve test verileri ile gerçek zamanlı senaryolarda bıçak ve silahları başarıyla tespit edebilmektedir. GPU desteği ile akıcı ve düşük gecikmeli çalışır.

## YOLOv8
- YOLOv8, önceki YOLO sürümlerinin başarısını temel alan, performansı ve esnekliği artıran yeni özellikler ve iyileştirmeler sunar. Hızlı ve doğru olmasının yanı sıra edge cihazlarda gerçek zamanlı çalışmaya uygundur.

![image](https://github.com/Puyz/weapon-knife-detection/assets/42616536/6be8e7c4-f445-414b-99c4-141a946447ac)

## ROBOFLOW
- Roboflow, verilerin etiketlenmesi ve yönetimi için kullanılan bir platformdur. YOLO formatında etiketleme yapılarak veri seti eğitim, doğrulama ve test olarak üçe ayrılmıştır. Bu süreç deneyleri hızlandırır ve veri kalitesini artırır.

![image](https://github.com/Puyz/weapon-knife-detection/assets/42616536/49995175-1992-4cb3-be37-a6a95d1c2dd5)

## SONUÇLAR
Aşağıda eğitimli modelden örnek tespit çıktıları yer almaktadır:

![image](https://github.com/Puyz/weapon-knife-detection/assets/42616536/58b18f73-00eb-4da9-9803-5d911f7b3a9d)

![image](https://github.com/Puyz/weapon-knife-detection/assets/42616536/8df0372e-4a36-40cb-a027-08c8e073b00a)

---

<a id="en"></a>

## 🇬🇧 English

# Knife and Firearm Detection in Video or Camera

## Problem Statement
- In security-critical environments, especially public areas, detecting knives and firearms is vital. There is a strong need for fast and accurate methods to identify such dangerous objects. This project aims to perform real-time detection of knives and firearms on video files and live camera streams.

## Solution
- We use the YOLOv8 object detection model. The model is trained on data labeled with Roboflow and can successfully detect knives and firearms on test data and real-time scenarios. With GPU support, inference runs smoothly with low latency.

## YOLOv8
- YOLOv8 builds on the success of previous YOLO versions and introduces improvements that boost both performance and flexibility. It is fast, accurate, and suitable for real-time deployment on edge devices.

![image](https://github.com/Puyz/weapon-knife-detection/assets/42616536/6be8e7c4-f445-414b-99c4-141a946447ac)

## Roboflow
- Roboflow is used for dataset preparation and labeling in YOLO format. The dataset is split into training, validation, and test sets, which streamlines experimentation and improves data quality.

![image](https://github.com/Puyz/weapon-knife-detection/assets/42616536/49995175-1992-4cb3-be37-a6a95d1c2dd5)

## Results
Below are sample detection outputs from the trained model:

![image](https://github.com/Puyz/weapon-knife-detection/assets/42616536/58b18f73-00eb-4da9-9803-5d911f7b3a9d)

![image](https://github.com/Puyz/weapon-knife-detection/assets/42616536/8df0372e-4a36-40cb-a027-08c8e073b00a)
