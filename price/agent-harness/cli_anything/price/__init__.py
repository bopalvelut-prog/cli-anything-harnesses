import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('price running')
@cli.command()
def start(): click.echo('price started')
if __name__ == '__main__': cli()
