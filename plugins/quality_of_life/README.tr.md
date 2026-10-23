# Quality of Life

[English](README.md) | [Türkçe](README.tr.md)

Günlük kullanım kontrolleri için küçük, isteğe bağlı iyileştirmeler.

| Ayar | Davranış |
| --- | --- |
| `ctrl_message_drag` | Mesaj aralığı seçmek için **Ctrl + sol tuşla sürükleme** gerektirir. Varsayılan olarak açıktır. |

Düz sürükleme, seçim modu zaten açıkken de mesaj seçimini başlatmaz veya genişletmez. Ctrl + sürükleme balonların yanındaki boşlukta, metinlerin ve eklerin üzerinde çalışır. Ctrl bırakılınca sürükleyerek seçim durur; seçilmiş mesajlar korunur. Normal metin seçimi, seçim kutuları, sağ tık menüsündeki seçim ve mevcut tıklama kısayolları kullanılmaya devam eder.

Ayarı veya eklentiyi kapatmak eski mesaj sürükleme davranışını geri getirir. İleride bu eklentiye bağımsız ayarlarla başka kullanım iyileştirmeleri eklenebilir.

`on_input_policy` kancasını içeren güncel API v3 host gerekir; eski host bu kancayı reddeder. Yalnız betiği kurmak yeni host yeteneğini eklemez. Bu kaynak klasörünü eklenti dizinine kopyalayıp eklentileri yeniden yükle. Yeni eklenti için ayrı public ZIP henüz yayımlanmadı.

[Kurulum](../../README.tr.md#kurulum)
