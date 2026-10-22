# ZapFast Eklentileri

[BenOnur/ZapFast](https://github.com/BenOnur/zapfast) için ayrı ayrı indirilebilen, isteğe bağlı yerel eklentiler. Her eklentinin kendi klasörü, manifesti ve Rhai dosyası var.

## Eklentiler ve indirme

| Eklenti | Ne yapar? | İndir | Kaynak / ayarlar |
| --- | --- | --- | --- |
| **Anti-Delete** | Yerelde alınmış silinen içerikleri korur; uygun ses/video dosyalarını saklar. | [anti_delete.zip](https://github.com/BenOnur/zapfast-plugins/releases/download/v1.1.0/anti_delete.zip) | [anti_delete](plugins/anti_delete/) |
| **Auto Responder** | Seçilen sohbetlerde tanımlanan komutlara ayarlanabilir gecikmeyle yanıt verir. | [auto_reply.zip](https://github.com/BenOnur/zapfast-plugins/releases/download/v1.1.0/auto_reply.zip) | [auto_reply](plugins/auto_reply/) |
| **Bildirim Aralığı** | Aynı kişi ve hesap için bildirimler arasında varsayılan 30 saniye bırakır. | [notification_throttle.zip](https://github.com/BenOnur/zapfast-plugins/releases/download/v1.1.0/notification_throttle.zip) | [notification_throttle](plugins/notification_throttle/) |
| **Quoter** | Mesaj sağ tık menüsünden ayarlanabilir alıntı kartı oluşturur. | [quoter.zip](https://github.com/BenOnur/zapfast-plugins/releases/download/v1.1.0/quoter.zip) | [quoter](plugins/quoter/) |
| **Hızlı Çıkartmalar** | Mesaj alanında emoji simgesinin hemen sağına, doğrudan çıkartmaları açan düğme ekler. | [quick_stickers.zip](https://github.com/BenOnur/zapfast-plugins/releases/download/v1.1.0/quick_stickers.zip) | [quick_stickers](plugins/quick_stickers/) |
| **bugfix** | Sohbet adının kullanılabilir genişliği doldurmasını sağlar; animasyon hazırlanırken çıkartmanın statik önizlemesini gösterir. Yeni düzeltmeler bu eklentiye eklenebilir. | [bugfix.zip](https://github.com/BenOnur/zapfast-plugins/releases/download/v1.1.0/bugfix.zip) | [bugfix](plugins/bugfix/) |

[Tüm sürümler ve SHA-256 dosyası](https://github.com/BenOnur/zapfast-plugins/releases).

## Uyumluluk

| Eklenti | Gereken host |
| --- | --- |
| Bildirim Aralığı | API v1 veya daha yeni yerel eklenti host'u. |
| Anti-Delete, Auto Responder, Quoter | API v2 veya daha yeni; yayımlanmış fork **v0.19.1** destekler. |
| Hızlı Çıkartmalar | API v3 ve `on_composer_tools`. |
| bugfix | API v3, `on_layout` ve `on_media_policy`. |

İlk dört eklenti [yayımlanmış fork v0.19.1](https://github.com/BenOnur/zapfast/releases/tag/v0.19.1) ile kullanılabilir ve bu host'ta ilk kurulumda zaten oluşturulur. Hızlı Çıkartmalar ve güncel bugfix için gerekli yeni host kodu [0f5a3b4](https://github.com/BenOnur/zapfast/commit/0f5a3b4) ve sonrasında bulunur. **Hazır API v3 uygulama paketi henüz yayımlanmadı**; bu son iki eklenti için kaynak sürümünden derlenmiş uyumlu host gerekir. Resmî upstream uygulamasında yerel eklenti host'u bulunmaz.

## Kurulum

1. Uyumlu ZapFast'te **Ayarlar → Plugins → Eklenti klasörünü aç** seçeneğini kullan.
2. İstediğin eklentinin ZIP dosyasını indir ve aç.
3. İçindeki eklenti klasörünü (`anti_delete`, `auto_reply`, `notification_throttle`, `quoter`, `quick_stickers` veya `bugfix`) açılan eklenti klasörüne kopyala.
4. **Yeniden yükle** düğmesine bas; eklentiyi ve istediğin ayarlarını aç.

Doğru klasör düzeni:

```text
plugins/
  anti_delete/
    plugin.json
    main.rhai
  auto_reply/
    plugin.json
    main.rhai
  notification_throttle/
    plugin.json
    main.rhai
  quoter/
    plugin.json
    main.rhai
  quick_stickers/
    plugin.json
    main.rhai
  bugfix/
    plugin.json
    main.rhai
```

Yalnız istediğin eklentileri kurabilirsin. Eklentileri Plugins ekranından kapatabilir veya klasörlerini kaldırıp yeniden yükleyebilirsin. Aynı eklentiyi güncellemeden önce kendi düzenlediğin dosyaları yedekle.

## bugfix ayarları

- **Sohbet adı kullanılabilir alanı doldursun:** Başlıkta sağ düğmelerin alanının iki kez çıkarılmasını giderir.
- **Çıkartmaları animasyonu beklemeden göster:** Yerel dosya hazırken animasyon çözümünü bekleyen çıkartmayı statik önizlemeyle gösterir; animasyon hazır olunca normal gösterime geçer. Henüz indirilmemiş dosyanın ağ beklemesini kaldırmaz.

## Geliştirme ve paketleme

Kaynaklar `plugins/<id>/` altında tutulur. Kullanıcı hesabı, sohbet arşivi ve kişisel ayarlar bu depoya dahil değildir.

```sh
python scripts/package.py
```

Komut her eklenti için `dist/<id>.zip` ve `dist/SHA256SUMS` üretir. ZIP yalnız ilgili klasör içindeki `plugin.json` ile `main.rhai` dosyalarını içerir. Dağıtılan sürümün host kaynak karşılığı ve kurulum ayrıntısı için sürüm notlarını oku.

Host API'si ve yerel doğrulama kodu: [ZapFast yerel eklenti belgeleri](https://github.com/BenOnur/zapfast/blob/main/docs/local-plugins.md). Desteklenen kancalardaki betik/ayar değişiklikleri yeniden derleme gerektirmez; yeni native yetenekler host güncellemesi gerektirir.

## Lisans

[MIT](LICENSE).
