import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('OpenWrt running')
@cli.command()
def wifi(): click.echo('WiFi status')
if __name__ == '__main__': cli()
