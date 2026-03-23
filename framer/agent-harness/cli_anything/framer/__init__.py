import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('framer running')
@cli.command()
def start(): click.echo('framer started')
if __name__ == '__main__': cli()
