import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('roller running')
@cli.command()
def start(): click.echo('roller started')
if __name__ == '__main__': cli()
