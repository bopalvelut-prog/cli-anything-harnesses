import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('dumbinit running')
@cli.command()
def start(): click.echo('dumbinit started')
if __name__ == '__main__': cli()
