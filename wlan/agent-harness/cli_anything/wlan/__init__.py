import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('wlan running')
@cli.command()
def start(): click.echo('wlan started')
if __name__ == '__main__': cli()
