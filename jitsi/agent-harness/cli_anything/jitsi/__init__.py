
import click, requests, json, os
@click.group()
def cli(): pass
JITSI = os.getenv('JITSI_URL', 'http://localhost:8080')
@cli.command()
def rooms():
    click.echo(f'Jitsi rooms endpoint: {JITSI}/room')
@cli.command()
@click.argument('room')
def meet(room): click.echo(f'{JITSI}/{room}')
if __name__ == '__main__': cli()
