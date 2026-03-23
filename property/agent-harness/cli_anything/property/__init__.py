import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('property running')
@cli.command()
def start(): click.echo('property started')
if __name__ == '__main__': cli()
