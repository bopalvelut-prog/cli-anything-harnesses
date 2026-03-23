import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('connector running')
@cli.command()
def start(): click.echo('connector started')
if __name__ == '__main__': cli()
