import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('notebook running')
@cli.command()
def start(): click.echo('notebook started')
if __name__ == '__main__': cli()
