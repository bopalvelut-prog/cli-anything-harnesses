import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('dish running')
@cli.command()
def start(): click.echo('dish started')
if __name__ == '__main__': cli()
