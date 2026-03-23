import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('visitor running')
@cli.command()
def start(): click.echo('visitor started')
if __name__ == '__main__': cli()
