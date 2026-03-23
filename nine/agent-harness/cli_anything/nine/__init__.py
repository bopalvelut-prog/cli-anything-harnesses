import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('nine running')
@cli.command()
def start(): click.echo('nine started')
if __name__ == '__main__': cli()
