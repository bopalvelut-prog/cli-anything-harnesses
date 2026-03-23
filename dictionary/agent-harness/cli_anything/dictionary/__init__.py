import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('dictionary running')
@cli.command()
def start(): click.echo('dictionary started')
if __name__ == '__main__': cli()
