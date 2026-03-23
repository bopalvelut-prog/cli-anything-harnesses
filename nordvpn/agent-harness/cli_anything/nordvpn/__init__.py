import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('nordvpn running')
@cli.command()
def start(): click.echo('nordvpn started')
if __name__ == '__main__': cli()
