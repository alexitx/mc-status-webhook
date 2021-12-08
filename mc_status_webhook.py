__author__ = 'alexitx'
__author_email__ = 'alexander@alexitx.com'
__license__ = 'MIT'
__title__ = 'mc-status-webhook'
__url__ = 'https://github.com/alexitx/mc-status-webhook'
__version__ = '0.1.0'


import logging
import logging.handlers
import os
import re
import sys
import socket
import time
from argparse import ArgumentParser, HelpFormatter
from discord_webhook import DiscordEmbed, DiscordWebhook
from mcstatus import MinecraftServer


log = logging.getLogger()


def error(msg=None, exc=None):
    if msg is not None:
        log.error(f'Error: {msg}')
    elif exc is not None:
        if str(exc):
            log.error(f'{type(exc).__name__}: {exc}')
        else:
            log.error(exc_info=exc)
    sys.exit(1)


def check_server_status(host, port):
    log.debug(f'Checking status for server {host}:{port}')
    server = MinecraftServer(host, port)
    try:
        latency = server.ping(1)
        log.debug(f'Received response from server, latency: {latency}ms')
        return True
    except (socket.timeout, ConnectionError):
        log.debug('Server is offline or unreachable')
    except Exception as e:
        if str(e):
            log.error(f'Error checking status: {type(e).__name__}: {e}')
        else:
            log.error('Error checking status', exc_info=e)
    return False


def send_webhook_status(
    server_is_online,
    webhook_url,
    thumbnail_url,
    online_color,
    offline_color,
    status_title,
    status_online_value,
    status_offline_value,
    address_title,
    address_value,
):
    log.debug(f"Creating webhook for '{webhook_url}'")
    webhook = DiscordWebhook(webhook_url, timeout=5)
    if server_is_online:
        embed = DiscordEmbed(title=status_title, description=status_online_value, color=online_color)
        if address_value is not None:
            embed.add_embed_field(name=address_title, value=address_value)
    else:
        embed = DiscordEmbed(title=status_title, description=status_offline_value, color=offline_color)
    if thumbnail_url is not None:
        embed.set_thumbnail(url=thumbnail_url)
    embed.set_timestamp()
    webhook.add_embed(embed)
    try:
        response = webhook.execute()
        response.raise_for_status() # pylint: disable=no-member
    except Exception as e:
        if str(e):
            log.error(f'Error executing webhook: {type(e).__name__}: {e}')
        else:
            log.error('Error executing webhook', exc_info=e)


def cli():

    class HelpFormatter_(HelpFormatter):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, max_help_position=48, **kwargs)

        def _format_action_invocation(self, action):
            if not action.option_strings or action.nargs == 0:
                return super()._format_action_invocation(action)
            default = self._get_default_metavar_for_optional(action)
            args_string = self._format_args(action, default)
            return f'{", ".join(action.option_strings)} {args_string}'

    parser = ArgumentParser(formatter_class=HelpFormatter_)
    main_group = parser.add_argument_group(title='Main arguments')
    main_group.add_argument(
        '-H',
        '--host',
        help='Server address (default: 127.0.0.1)',
        metavar='<host>'
    )
    main_group.add_argument(
        '-p',
        '--port',
        type=int,
        help='Server port (default: 25565)',
        metavar='<port>'
    )
    main_group.add_argument(
        '-t',
        '--update-time',
        default=10.0,
        type=float,
        help='Time in seconds between checking the server status (default: 10)',
        metavar='<seconds>'
    )
    main_group.add_argument(
        '-u',
        '--webhook-url',
        help='Discord webhook URL',
        metavar='<url>'
    )
    main_group.add_argument(
        '-d',
        '--debug',
        action='store_true',
        help='Log debug messages',
    )
    webhook_group = parser.add_argument_group(title='Webhook arguments')
    webhook_group.add_argument(
        '--thumbnail-url',
        help='Webhook thumbnail URL',
        metavar='<url>'
    )
    webhook_group.add_argument(
        '--online-color',
        help="Webhook color hex when the server is online (default: '30c030')",
        metavar='<color>'
    )
    webhook_group.add_argument(
        '--offline-color',
        help="Webhook color hex when the server is offline (default: 'ff4040')",
        metavar='<color>'
    )
    webhook_group.add_argument(
        '--status-title',
        help="Webhook status title (default: 'Status')",
        metavar='<title>'
    )
    webhook_group.add_argument(
        '--status-online-value',
        help="Webhook status value when the server is online (default: 'Online')",
        metavar='<value>'
    )
    webhook_group.add_argument(
        '--status-offline-value',
        help="Webhook status value when the server is offline (default: 'Offline')",
        metavar='<value>'
    )
    webhook_group.add_argument(
        '--address-title',
        help="Webhook address title (default: 'Address')",
        metavar='<title>'
    )
    webhook_group.add_argument(
        '--address-value',
        help='Webhook address value when the server is online',
        metavar='<value>'
    )
    args = parser.parse_args()

    formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(message)s')
    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(formatter)
    log.addHandler(handler)
    log.setLevel(logging.DEBUG if args.debug else logging.INFO)

    def args_default(arg, default):
        return arg if arg is not None else default

    host = args_default(args.host, os.environ.get('MSW_HOST', '127.0.0.1'))
    port = args_default(args.port, os.environ.get('MSW_PORT', '25565'))
    webhook_url = args_default(args.webhook_url, os.environ.get('MSW_WEBHOOK_URL'))
    thumbnail_url = args_default(args.thumbnail_url, os.environ.get('MSW_THUMBNAIL_URL'))
    online_color = args_default(args.online_color, os.environ.get('MSW_ONLINE_COLOR', '30c030'))
    offline_color = args_default(args.offline_color, os.environ.get('MSW_OFFLINE_COLOR', 'ff4040'))
    status_title = args_default(args.status_title, os.environ.get('MSW_STATUS_TITLE', 'Status'))
    status_online_value = args_default(args.status_online_value, os.environ.get('MSW_STATUS_ONLINE_VALUE', 'Online'))
    status_offline_value = args_default(args.status_offline_value, os.environ.get('MSW_STATUS_OFFLINE_VALUE', 'Offline'))
    address_title = args_default(args.address_title, os.environ.get('MSW_ADDRESS_TITLE', 'Address'))
    address_value = args_default(args.address_value, os.environ.get('MSW_ADDRESS_VALUE'))

    try:
        port = int(port)
    except ValueError:
        parser.error(f"Invalid port '{port}'")
    if not 1 <= port <= 65535:
        parser.error('Port must be within range of 1-65535')

    if args.update_time <= 0:
        parser.error('Update time must be a positive number')

    if webhook_url is None:
        parser.error('Webhook URL must be specified')

    color_re = re.compile(r'^[a-f0-9]{6}$', re.IGNORECASE)
    if not color_re.match(online_color):
        parser.error(f"Invalid online color hex value '{online_color}'")
    if not color_re.match(offline_color):
        parser.error(f"Invalid offline color hex value '{offline_color}'")

    log.debug(
        'Parsed arguments:\n'
        f'{host=}\n'
        f'{port=}\n'
        f'{args.update_time=}\n'
        f'{webhook_url=}\n'
        f'{args.debug=}\n'
        f'{thumbnail_url=}\n'
        f'{online_color=}\n'
        f'{offline_color=}\n'
        f'{status_title=}\n'
        f'{status_online_value=}\n'
        f'{status_offline_value=}\n'
        f'{address_title=}\n'
        f'{address_value=}'
    )

    online_last = check_server_status(host, port)
    while True:
        time.sleep(args.update_time)
        online_now = check_server_status(host, port)
        if online_now == online_last:
            continue
        online_last = online_now
        server_status = 'Online' if online_now else 'Offline'
        log.info(f'Server status changed to: {server_status}')
        send_webhook_status(
            online_now,
            webhook_url,
            thumbnail_url,
            online_color,
            offline_color,
            status_title,
            status_online_value,
            status_offline_value,
            address_title,
            address_value
        )


def main():
    try:
        cli()
    except KeyboardInterrupt:
        print('Exiting')
        sys.exit(1)


if __name__ == '__main__':
    main()
