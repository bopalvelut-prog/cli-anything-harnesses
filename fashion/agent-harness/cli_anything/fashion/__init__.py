import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('fashion running')
@cli.command()
def start(): click.echo('fashion started')
if __name__ == '__main__': cli()
