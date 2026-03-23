import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('painting running')
@cli.command()
def start(): click.echo('painting started')
if __name__ == '__main__': cli()
