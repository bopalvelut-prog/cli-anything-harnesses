import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('sophisticated running')
@cli.command()
def start(): click.echo('sophisticated started')
if __name__ == '__main__': cli()
