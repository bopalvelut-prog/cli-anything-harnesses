import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('quantlib running')
@cli.command()
def start(): click.echo('quantlib started')
if __name__ == '__main__': cli()
