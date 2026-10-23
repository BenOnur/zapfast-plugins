# Quality of Life

[English](README.md) | [Türkçe](README.tr.md)

Small, optional improvements for everyday controls.

| Setting | Behavior |
| --- | --- |
| `ctrl_message_drag` | Requires **Ctrl + left-button drag** to select a range of messages. Enabled by default. |

Plain dragging no longer starts or extends message selection, even when selection mode is already open. Ctrl-drag works beside bubbles, over text and over attachments. Releasing Ctrl stops the sweep and keeps the messages already selected. Ordinary text selection, checkboxes, context-menu selection and existing click shortcuts remain available.

Disable the setting or plugin to restore the original message-drag behavior. Later improvements can be added here as independent settings.

Requires an updated API v3 host with `on_input_policy`; older hosts reject this hook. Installing the script alone cannot add that host capability. Copy this source folder into your plugin directory, then reload plugins. A standalone public ZIP for this new plugin has not been released yet.

[Installation](../../README.md#installation)
