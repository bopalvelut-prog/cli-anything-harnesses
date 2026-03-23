import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('plantuml running')
@cli.command()
def start(): click.echo('plantuml started')
if __name__ == '__main__': cli()
