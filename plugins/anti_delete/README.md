# Anti-Delete

[English](README.md) | [Türkçe](README.tr.md)

Retains locally received content when a message is deleted. Proactively downloads eligible new audio/video within the configured limit. It cannot recover content never received. Disabling it stops future retention; it does not erase previously retained files.

- Host: API v2 or newer; fork v0.19.1 is supported.
- `retain`: retain newly deleted content; enabled by default.
- `max_media_mib`: 64 MiB by default; the host also enforces its own 64 MiB limit.

[Download](https://github.com/BenOnur/zapfast-plugins/releases/download/v1.1.0/anti_delete.zip) | [Installation](../../README.md#installation)
