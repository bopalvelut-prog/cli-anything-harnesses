import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('clip running')
@cli.command()
def start(): click.echo('clip started')
if __name__ == '__main__': cli()
