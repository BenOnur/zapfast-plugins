# bugfix

Birden fazla düzeltmeyi ayrı ayarlarla barındıran genel eklenti.

| Ayar | Davranış |
| --- | --- |
| `header_title_width` | Sohbet adının sağ düğmelere kadar kalan alanı kullanmasını sağlar. |
| `sticker_preview` | Yerel hareketli çıkartmanın önizlemesini tüm animasyon çözülmeden gösterir; ilk istekte önce tek kare hazırlanır. Gelen ve gönderilen çıkartmalara uygulanır. |

İki ayar da varsayılan olarak açıktır. Ayrı ayrı veya eklentinin tamamı kapatılabilir. `sticker_preview` dosyanın ağdan indirilme süresini kaldırmaz.

Gerekli kancalar: API v3 `on_layout` ve `on_media_policy`. İkincisi eklendiği için eski API v3 host'ları da bu güncelleme için yeterli olmayabilir; [host uyumluluğunu kontrol et](../../README.md#uyumluluk).

[İndir](https://github.com/BenOnur/zapfast-plugins/releases/download/v1.1.0/bugfix.zip) · [Kurulum](../../README.md#kurulum)
