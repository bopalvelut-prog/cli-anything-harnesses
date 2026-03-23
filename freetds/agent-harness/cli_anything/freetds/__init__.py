import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('freetds running')
@cli.command()
def start(): click.echo('freetds started')
if __name__ == '__main__': cli()
