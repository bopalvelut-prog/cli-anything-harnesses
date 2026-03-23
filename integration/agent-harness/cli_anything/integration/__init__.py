import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('integration running')
@cli.command()
def start(): click.echo('integration started')
if __name__ == '__main__': cli()
