import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('nova running')
@cli.command()
def start(): click.echo('nova started')
if __name__ == '__main__': cli()
