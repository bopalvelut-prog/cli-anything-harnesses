import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('scroll running')
@cli.command()
def start(): click.echo('scroll started')
if __name__ == '__main__': cli()
