import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('lady running')
@cli.command()
def start(): click.echo('lady started')
if __name__ == '__main__': cli()
