import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('joke running')
@cli.command()
def start(): click.echo('joke started')
if __name__ == '__main__': cli()
