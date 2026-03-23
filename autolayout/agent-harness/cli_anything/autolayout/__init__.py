import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('autolayout running')
@cli.command()
def start(): click.echo('autolayout started')
if __name__ == '__main__': cli()
