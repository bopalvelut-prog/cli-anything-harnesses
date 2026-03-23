import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('breast running')
@cli.command()
def start(): click.echo('breast started')
if __name__ == '__main__': cli()
