import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('gson running')
@cli.command()
def start(): click.echo('gson started')
if __name__ == '__main__': cli()
