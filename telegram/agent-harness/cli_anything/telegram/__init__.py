
import click, requests, os
@click.group()
def cli(): pass
BOT = os.getenv('TELEGRAM_BOT_TOKEN', '')
@cli.command()
@click.argument('chat_id')
@click.argument('text')
def send(chat_id, text):
    if not BOT: click.echo('Set TELEGRAM_BOT_TOKEN'); return
    requests.post(f'https://api.telegram.org/bot{BOT}/sendMessage', json={'chat_id': chat_id, 'text': text})
    click.echo('Sent')
@cli.command()
def updates():
    if not BOT: return
    r = requests.get(f'https://api.telegram.org/bot{BOT}/getUpdates')
    click.echo(r.json())
if __name__ == '__main__': cli()
