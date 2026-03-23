import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('apex running')
@cli.command()
def start(): click.echo('apex started')
if __name__ == '__main__': cli()
