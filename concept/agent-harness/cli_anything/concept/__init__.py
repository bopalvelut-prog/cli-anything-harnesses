import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('concept running')
@cli.command()
def start(): click.echo('concept started')
if __name__ == '__main__': cli()
