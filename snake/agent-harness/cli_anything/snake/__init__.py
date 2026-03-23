import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('snake running')
@cli.command()
def start(): click.echo('snake started')
if __name__ == '__main__': cli()
