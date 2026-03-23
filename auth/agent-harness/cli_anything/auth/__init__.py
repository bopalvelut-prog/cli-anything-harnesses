import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('auth running')
@cli.command()
def start(): click.echo('auth started')
if __name__ == '__main__': cli()
