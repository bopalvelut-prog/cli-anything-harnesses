import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('adventure running')
@cli.command()
def start(): click.echo('adventure started')
if __name__ == '__main__': cli()
