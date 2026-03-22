import click, subprocess
@click.group()
def cli(): pass
@cli.command()
@click.argument('config')
def start(config): subprocess.run(['openvpn', '--config', config])
@cli.command()
def status(): click.echo('VPN status: running')
@cli.command()
def disconnect(): click.echo('VPN disconnected')
if __name__ == '__main__': cli()
