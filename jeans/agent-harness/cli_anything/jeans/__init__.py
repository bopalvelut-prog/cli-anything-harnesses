import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('jeans running')
@cli.command()
def start(): click.echo('jeans started')
if __name__ == '__main__': cli()
