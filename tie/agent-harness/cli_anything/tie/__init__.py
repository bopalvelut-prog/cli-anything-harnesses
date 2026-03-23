import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('tie running')
@cli.command()
def start(): click.echo('tie started')
if __name__ == '__main__': cli()
