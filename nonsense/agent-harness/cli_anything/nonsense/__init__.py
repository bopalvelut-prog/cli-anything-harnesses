import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('nonsense running')
@cli.command()
def start(): click.echo('nonsense started')
if __name__ == '__main__': cli()
