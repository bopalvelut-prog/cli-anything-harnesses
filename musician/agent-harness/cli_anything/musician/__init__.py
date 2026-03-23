import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('musician running')
@cli.command()
def start(): click.echo('musician started')
if __name__ == '__main__': cli()
