import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('digikey running')
@cli.command()
def start(): click.echo('digikey started')
if __name__ == '__main__': cli()
