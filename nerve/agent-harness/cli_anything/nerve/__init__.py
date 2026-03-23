import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('nerve running')
@cli.command()
def start(): click.echo('nerve started')
if __name__ == '__main__': cli()
