import click, subprocess
@click.group()
def cli(): pass
@cli.command()
@click.argument('bssid')
def wps(bssid): subprocess.run(['reaver', '-i', 'wlan0mon', '-b', bssid, '-vv'])
if __name__ == '__main__': cli()
