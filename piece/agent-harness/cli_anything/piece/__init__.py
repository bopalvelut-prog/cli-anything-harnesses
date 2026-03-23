import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('piece running')
@cli.command()
def start(): click.echo('piece started')
if __name__ == '__main__': cli()
