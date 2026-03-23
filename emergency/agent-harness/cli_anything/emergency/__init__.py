import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('emergency running')
@cli.command()
def start(): click.echo('emergency started')
if __name__ == '__main__': cli()
