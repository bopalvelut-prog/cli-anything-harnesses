import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('shape running')
@cli.command()
def start(): click.echo('shape started')
if __name__ == '__main__': cli()
