import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('array running')
@cli.command()
def start(): click.echo('array started')
if __name__ == '__main__': cli()
