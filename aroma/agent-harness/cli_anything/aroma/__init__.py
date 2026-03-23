import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('aroma running')
@cli.command()
def start(): click.echo('aroma started')
if __name__ == '__main__': cli()
