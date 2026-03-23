import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('joint running')
@cli.command()
def start(): click.echo('joint started')
if __name__ == '__main__': cli()
