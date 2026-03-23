import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('realize running')
@cli.command()
def start(): click.echo('realize started')
if __name__ == '__main__': cli()
