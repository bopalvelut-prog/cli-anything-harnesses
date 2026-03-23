import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('immutant running')
@cli.command()
def start(): click.echo('immutant started')
if __name__ == '__main__': cli()
