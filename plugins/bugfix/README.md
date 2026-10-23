# bugfix

[English](README.md) | [Türkçe](README.tr.md)

A general plugin containing independently configurable fixes.

| Setting | Behavior |
| --- | --- |
| `header_title_width` | Lets the chat title use the remaining space before the right-hand buttons. |
| `sticker_preview` | Shows a downloaded animated sticker's preview before the full animation is decoded; the first request prepares a single frame first. Applies to sent and received stickers. |

Both settings default to enabled. Disable each separately or disable the entire plugin. `sticker_preview` does not eliminate the network time needed to download a file.

Required hooks: API v3 `on_layout` and `on_media_policy`. Older API v3 hosts may lack the latter; check [host compatibility](../../README.md#compatibility).

[Download](https://github.com/BenOnur/zapfast-plugins/releases/download/v1.1.0/bugfix.zip) | [Installation](../../README.md#installation)
