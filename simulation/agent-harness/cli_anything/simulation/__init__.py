import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('simulation running')
@cli.command()
def start(): click.echo('simulation started')
if __name__ == '__main__': cli()
