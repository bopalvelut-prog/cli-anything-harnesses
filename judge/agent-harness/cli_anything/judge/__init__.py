import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('judge running')
@cli.command()
def start(): click.echo('judge started')
if __name__ == '__main__': cli()
