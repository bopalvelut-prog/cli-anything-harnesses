import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('hostapd running')
@cli.command()
def start(): click.echo('hostapd started')
if __name__ == '__main__': cli()
