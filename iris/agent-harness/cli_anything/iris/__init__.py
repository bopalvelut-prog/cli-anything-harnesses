import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('iris running')
@cli.command()
def start(): click.echo('iris started')
if __name__ == '__main__': cli()
