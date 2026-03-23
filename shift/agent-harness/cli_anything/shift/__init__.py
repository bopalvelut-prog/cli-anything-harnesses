import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('shift running')
@cli.command()
def start(): click.echo('shift started')
if __name__ == '__main__': cli()
