import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('novel running')
@cli.command()
def start(): click.echo('novel started')
if __name__ == '__main__': cli()
