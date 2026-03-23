import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('swap running')
@cli.command()
def start(): click.echo('swap started')
if __name__ == '__main__': cli()
