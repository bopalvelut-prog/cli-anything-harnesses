import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('hello running')
@cli.command()
def start(): click.echo('hello started')
if __name__ == '__main__': cli()
