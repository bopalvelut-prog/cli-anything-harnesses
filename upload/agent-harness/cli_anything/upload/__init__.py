import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('upload running')
@cli.command()
def start(): click.echo('upload started')
if __name__ == '__main__': cli()
