# ZapFast Eklentileri

[BenOnur/ZapFast](https://github.com/BenOnur/zapfast) için ayrı ayrı indirilebilen, isteğe bağlı yerel eklentiler. Her eklentinin kendi klasörü, manifesti ve Rhai dosyası var.

## Eklentiler ve indirme

| Eklenti | Ne yapar? | İndir | Kaynak / ayarlar |
| --- | --- | --- | --- |
| **Hızlı Çıkartmalar** | Mesaj alanında emoji simgesinin hemen sağına, doğrudan çıkartmaları açan düğme ekler. | [quick_stickers.zip](https://github.com/BenOnur/zapfast-plugins/releases/download/v1.0.0/quick_stickers.zip) | [quick_stickers](plugins/quick_stickers/) |
| **bugfix** | Sohbet adının kullanılabilir genişliği doldurmasını sağlar; animasyon hazırlanırken çıkartmanın statik önizlemesini gösterir. Yeni düzeltmeler bu eklentiye eklenebilir. | [bugfix.zip](https://github.com/BenOnur/zapfast-plugins/releases/download/v1.0.0/bugfix.zip) | [bugfix](plugins/bugfix/) |

[Tüm sürümler ve SHA-256 dosyası](https://github.com/BenOnur/zapfast-plugins/releases).

## Uyumluluk

**API v3 destekli eklenti host'u gerekir.** Gerekli host kodu [ZapFast fork'unda 0f5a3b4](https://github.com/BenOnur/zapfast/commit/0f5a3b4) ve sonrasında bulunur. `bugfix`, `on_layout` ve `on_media_policy`; Hızlı Çıkartmalar, `on_composer_tools` kancalarını kullanır.

Yayımlanmış **ZapFast v0.19.1 / API v2 bu eklentileri desteklemez**. API v3 içeren hazır uygulama paketi henüz yayımlanmadı; şu an uyumlu fork kaynağından derlenmiş uygulama gerekir. Resmî upstream uygulamasında bu yerel eklenti host'u bulunmaz.

## Kurulum

1. Uyumlu ZapFast'te **Ayarlar → Plugins → Eklenti klasörünü aç** seçeneğini kullan.
2. İstediğin eklentinin ZIP dosyasını indir ve aç.
3. İçindeki `quick_stickers` veya `bugfix` klasörünü açılan eklenti klasörüne kopyala.
4. **Yeniden yükle** düğmesine bas; eklentiyi ve istediğin ayarlarını aç.

Doğru klasör düzeni:

```text
plugins/
  quick_stickers/
    plugin.json
    main.rhai
  bugfix/
    plugin.json
    main.rhai
```

İkisini birlikte kurmak zorunda değilsin. Eklentileri Plugins ekranından kapatabilir veya klasörlerini kaldırıp yeniden yükleyebilirsin. Aynı eklentiyi güncellemeden önce kendi düzenlediğin dosyaları yedekle.

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
