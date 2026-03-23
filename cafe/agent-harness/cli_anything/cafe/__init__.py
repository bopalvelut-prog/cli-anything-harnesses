import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('cafe running')
@cli.command()
def start(): click.echo('cafe started')
if __name__ == '__main__': cli()
