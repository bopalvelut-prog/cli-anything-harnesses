import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('except running')
@cli.command()
def start(): click.echo('except started')
if __name__ == '__main__': cli()
