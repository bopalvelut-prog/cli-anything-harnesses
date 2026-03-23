import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('unlock running')
@cli.command()
def start(): click.echo('unlock started')
if __name__ == '__main__': cli()
