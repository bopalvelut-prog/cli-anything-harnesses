import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('alchemist running')
@cli.command()
def start(): click.echo('alchemist started')
if __name__ == '__main__': cli()
