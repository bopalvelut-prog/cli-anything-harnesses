import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('jwt running')
@cli.command()
def start(): click.echo('jwt started')
if __name__ == '__main__': cli()
