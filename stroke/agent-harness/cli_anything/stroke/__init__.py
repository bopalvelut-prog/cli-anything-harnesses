import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('stroke running')
@cli.command()
def start(): click.echo('stroke started')
if __name__ == '__main__': cli()
