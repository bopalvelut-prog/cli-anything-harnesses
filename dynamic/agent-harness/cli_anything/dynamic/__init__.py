import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('dynamic running')
@cli.command()
def start(): click.echo('dynamic started')
if __name__ == '__main__': cli()
