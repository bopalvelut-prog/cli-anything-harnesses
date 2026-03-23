import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('drama running')
@cli.command()
def start(): click.echo('drama started')
if __name__ == '__main__': cli()
