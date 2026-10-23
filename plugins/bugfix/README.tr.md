# bugfix

[English](README.md) | [Türkçe](README.tr.md)

Birden fazla düzeltmeyi ayrı ayarlarla barındıran genel eklenti.

| Ayar | Davranış |
| --- | --- |
| `header_title_width` | Sohbet adının sağ düğmelere kadar kalan alanı kullanmasını sağlar. |
| `message_row_width` | Eski mesajlarda kaydırırken, kendinle sohbet dahil, giden mesajları görünür alan içinde tutar. `message_row` bölgesini sunan yeni host gerekir. |
| `sticker_preview` | Yerel hareketli çıkartmanın önizlemesini tüm animasyon çözülmeden gösterir; ilk istekte önce tek kare hazırlanır. Gelen ve gönderilen çıkartmalara uygulanır. |

Üç ayar da varsayılan olarak açıktır. Ayrı ayrı veya eklentinin tamamı kapatılabilir. `sticker_preview` dosyanın ağdan indirilme süresini kaldırmaz.

Gerekli kancalar: API v3 `on_layout` ve `on_media_policy`. İkincisi eklendiği için eski API v3 host'ları da bu güncelleme için yeterli olmayabilir; [host uyumluluğunu kontrol et](../../README.tr.md#uyumluluk).

[İndir](https://github.com/BenOnur/zapfast-plugins/releases/download/v1.1.0/bugfix.zip) · [Kurulum](../../README.tr.md#kurulum)

`message_row_width` düzeltmesi güncel kaynakta bulunur; yukarıdaki v1.1.0 ZIP bu düzeltmeden önce yayımlandı. Eski hostta yalnız betiği güncellemek bu çizim yeteneğini eklemez.
