import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('airvpn running')
@cli.command()
def start(): click.echo('airvpn started')
if __name__ == '__main__': cli()
