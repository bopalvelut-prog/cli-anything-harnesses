import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('sample running')
@cli.command()
def start(): click.echo('sample started')
if __name__ == '__main__': cli()
