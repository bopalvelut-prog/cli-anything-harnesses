import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('transportation running')
@cli.command()
def start(): click.echo('transportation started')
if __name__ == '__main__': cli()
