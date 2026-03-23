import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('tone running')
@cli.command()
def start(): click.echo('tone started')
if __name__ == '__main__': cli()
