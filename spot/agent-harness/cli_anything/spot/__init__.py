import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('spot running')
@cli.command()
def start(): click.echo('spot started')
if __name__ == '__main__': cli()
