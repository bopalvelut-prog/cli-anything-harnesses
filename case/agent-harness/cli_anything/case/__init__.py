import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('case running')
@cli.command()
def start(): click.echo('case started')
if __name__ == '__main__': cli()
