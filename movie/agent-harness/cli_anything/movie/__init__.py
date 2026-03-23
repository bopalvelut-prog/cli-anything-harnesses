import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('movie running')
@cli.command()
def start(): click.echo('movie started')
if __name__ == '__main__': cli()
