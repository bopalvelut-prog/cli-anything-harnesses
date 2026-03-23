import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('maison running')
@cli.command()
def start(): click.echo('maison started')
if __name__ == '__main__': cli()
