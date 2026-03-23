import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('reserve running')
@cli.command()
def start(): click.echo('reserve started')
if __name__ == '__main__': cli()
