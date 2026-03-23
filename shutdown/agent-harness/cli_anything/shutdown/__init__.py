import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('shutdown running')
@cli.command()
def start(): click.echo('shutdown started')
if __name__ == '__main__': cli()
