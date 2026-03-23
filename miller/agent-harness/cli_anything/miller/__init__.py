import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('miller running')
@cli.command()
def start(): click.echo('miller started')
if __name__ == '__main__': cli()
