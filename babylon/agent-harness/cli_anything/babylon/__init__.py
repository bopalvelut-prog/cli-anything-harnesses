import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('babylon running')
@cli.command()
def start(): click.echo('babylon started')
if __name__ == '__main__': cli()
