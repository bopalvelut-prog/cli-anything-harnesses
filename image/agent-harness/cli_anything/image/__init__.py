import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('image running')
@cli.command()
def start(): click.echo('image started')
if __name__ == '__main__': cli()
