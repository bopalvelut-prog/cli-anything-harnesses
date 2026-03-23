import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('bats running')
@cli.command()
def start(): click.echo('bats started')
if __name__ == '__main__': cli()
