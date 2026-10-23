# ZapFast Plugins

[English](README.md) | [Türkçe](README.tr.md)

Optional local plugins for [BenOnur/ZapFast](https://github.com/BenOnur/zapfast), available as separate downloads. Each plugin has its own folder, manifest, Rhai script, and documentation.

## Plugins and downloads

| Plugin | What it does | Download | Source and settings |
| --- | --- | --- | --- |
| **Anti-Delete** | Retains deleted content already received locally and caches eligible audio/video. | [anti_delete.zip](https://github.com/BenOnur/zapfast-plugins/releases/download/v1.1.0/anti_delete.zip) | [anti_delete](plugins/anti_delete/) |
| **Auto Responder** | Replies to configured text commands in selected chats after an adjustable delay. | [auto_reply.zip](https://github.com/BenOnur/zapfast-plugins/releases/download/v1.1.0/auto_reply.zip) | [auto_reply](plugins/auto_reply/) |
| **Notification Throttle** | Leaves a configurable interval between notifications from the same sender and account; 30 seconds by default. | [notification_throttle.zip](https://github.com/BenOnur/zapfast-plugins/releases/download/v1.1.0/notification_throttle.zip) | [notification_throttle](plugins/notification_throttle/) |
| **Quoter** | Creates customizable quote cards from a message's context menu. | [quoter.zip](https://github.com/BenOnur/zapfast-plugins/releases/download/v1.1.0/quoter.zip) | [quoter](plugins/quoter/) |
| **Quick Stickers** | Adds a button immediately to the right of emoji that opens the Stickers tab directly. | [quick_stickers.zip](https://github.com/BenOnur/zapfast-plugins/releases/download/v1.1.0/quick_stickers.zip) | [quick_stickers](plugins/quick_stickers/) |
| **bugfix** | Lets the chat title use the available header width and displays a static sticker preview while animation decoding finishes. Further fixes can be added here. | [bugfix.zip](https://github.com/BenOnur/zapfast-plugins/releases/download/v1.1.0/bugfix.zip) | [bugfix](plugins/bugfix/) |

[All releases and SHA-256 checksums](https://github.com/BenOnur/zapfast-plugins/releases).

## Compatibility

| Plugin | Required host |
| --- | --- |
| Notification Throttle | Local plugin API v1 or newer. |
| Anti-Delete, Auto Responder, Quoter | API v2 or newer; the published fork **v0.19.1** supports them. |
| Quick Stickers | API v3 with `on_composer_tools`. |
| bugfix | API v3 with `on_layout` and `on_media_policy`. |

The first four plugins work with [fork v0.19.1](https://github.com/BenOnur/zapfast/releases/tag/v0.19.1) and are already seeded on that host's first migration. The host code required by Quick Stickers and current bugfix is available at [0f5a3b4](https://github.com/BenOnur/zapfast/commit/0f5a3b4) and later. **A ready-to-download API v3 application package has not been published yet**; those last two plugins currently require a compatible build from the fork's source. Official upstream builds do not contain this local plugin host.

## Installation

1. In a compatible ZapFast build, open **Settings > Plugins** and select **Eklenti klasörünü aç** (open plugin folder; the current host displays this label in Turkish).
2. Download and extract the ZIP for the plugin you want.
3. Copy its folder (`anti_delete`, `auto_reply`, `notification_throttle`, `quoter`, `quick_stickers`, or `bugfix`) into the plugin directory.
4. Select **Yeniden yükle** (reload) and enable the plugin and its desired settings. The current host displays this button in Turkish as well.

Expected directory layout:

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

Install only the plugins you want. Disable them in Plugins, or remove their folders and reload. Back up your own file edits before updating an existing plugin.

## bugfix settings

- **`header_title_width`:** Lets the chat title fill the remaining header width by avoiding a second reservation for the right-hand controls.
- **`sticker_preview`:** Shows a static preview of a downloaded sticker while animation decoding finishes, then switches to the normal animation. It does not remove the network wait for files that have not downloaded yet.

## Development and packaging

Sources live in `plugins/<id>/`. The repository does not contain user accounts, chat archives, or personal settings.

```sh
python scripts/package.py
```

This creates `dist/<id>.zip` for each plugin and `dist/SHA256SUMS`. Each ZIP contains only that plugin's `plugin.json` and `main.rhai`. Consult release notes for the corresponding host source and installation requirements.

Host API and validation code: [ZapFast local plugin documentation](https://github.com/BenOnur/zapfast/blob/main/docs/local-plugins.md). Script and setting changes within supported hooks reload without recompilation; new native capabilities require a host update.

## License

[MIT](LICENSE).
