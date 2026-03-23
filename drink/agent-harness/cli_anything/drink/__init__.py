import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('drink running')
@cli.command()
def start(): click.echo('drink started')
if __name__ == '__main__': cli()
