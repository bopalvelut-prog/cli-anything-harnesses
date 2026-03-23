import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('art running')
@cli.command()
def start(): click.echo('art started')
if __name__ == '__main__': cli()
