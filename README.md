# Minecraft server status webhook for Discord

Poll a server and send customizable webhook embed if the status changes.

Requires Python 3.6+

## Table of contents
- [Installation](#installation)
- [Usage](#usage)
  - [CLI arguments](#cli-arguments)
  - [Environment variables](#environment-variables)
- [License](#license)

## Installation

###### Use `python` on Windows instead of `python3`

Update pip and dependencies
```sh
$ python3 -m pip install --upgrade pip
$ python3 -m pip install --upgrade setuptools wheel
```
Install
```sh
$ python3 -m pip install git+https://github.com/alexitx/mc-status-webhook.git
```

## Usage

```sh
$ python3 mc_status_webhook.py -u "<webhook url>" [options]
```
or set the appropriate environment variables.

See [CLI arguments](#cli-arguments) and [Environment variables](#environment-variables)
for configuration.

Example scripts are also provided in the 'examples' directory.
Get [msw-example.cmd][windows-script] for Windows or [msw-example.sh][linux-script]
for Linux and modify it to your needs.

> **Note:** It is strongly recommended to run mc-status-webhook on the same machine or local network
> as the Minecraft server to avoid false notifications due to connection issues and wasting
> bandwidth. In this case use the loopback address 127.0.0.1 or the local address of the machine.

### CLI arguments

| Argument               | Type  | Default         | Required | Description                                                          |
|------------------------|-------|-----------------|----------|----------------------------------------------------------------------|
| -H, --host             | str   | 127.0.0.1       | No       | Server address                                                       |
| -p, --port             | int   | 25565           | No       | Server port                                                          |
| -t, --update-time      | float | 10.0            | No       | Time in seconds between checking the server status                   |
| -i, --initial-status   | bool  |                 | No       | Send a webhook with the server status on application start           |
| -u, --webhook-url      | str   |                 | Yes      | Discord webhook URL                                                  |
| -d, --debug            | bool  |                 | No       | Log debug messages                                                   |
| --online-thumb-url     | str   | \<online icon>  | No       | Webhook thumbnail URL when the server is online ('none' = disabled)  |
| --offline-thumb-url    | str   | \<offline icon> | No       | Webhook thumbnail URL when the server is offline ('none' = disabled) |
| --online-color         | str   | 30c030          | No       | Webhook color hex when the server is online                          |
| --offline-color        | str   | ff4040          | No       | Webhook color hex when the server is offline                         |
| --status-title         | str   | Status          | No       | Webhook status title                                                 |
| --status-online-value  | str   | Online          | No       | Webhook status value when the server is online                       |
| --status-offline-value | str   | Offline         | No       | Webhook status value when the server is offline                      |
| --address-title        | str   | Address         | No       | Webhook address title                                                |
| --address-value        | str   |                 | No       | Webhook address value when the server is online                      |

### Environment variables

| Environment variable     | Equivalent argument     |
|--------------------------|-------------------------|
| MSW_HOST                 | -H, --host              |
| MSW_PORT                 | -p, --port              |
| MSW_WEBHOOK_URL          | -u, --webhook-url       |
| MSW_ONLINE_THUMB_URL     | --online-thumbnail-url  |
| MSW_OFFLINE_THUMB_URL    | --offline-thumbnail-url |
| MSW_ONLINE_COLOR         | --online-color          |
| MSW_OFFLINE_COLOR        | --offline-color         |
| MSW_STATUS_TITLE         | --status-title          |
| MSW_STATUS_ONLINE_VALUE  | --status-online-value   |
| MSW_STATUS_OFFLINE_VALUE | --status-offline-value  |
| MSW_ADDRESS_TITLE        | --address-title         |
| MSW_ADDRESS_VALUE        | --address-value         |

## License

MIT license. See [LICENSE][license] for more information.

[windows-script]: https://github.com/alexitx/mc-status-webhook/raw/master/examples/msw-example.cmd
[linux-script]: https://github.com/alexitx/mc-status-webhook/raw/master/examples/msw-example.sh
[license]: https://github.com/alexitx/mc-status-webhook/blob/master/LICENSE
