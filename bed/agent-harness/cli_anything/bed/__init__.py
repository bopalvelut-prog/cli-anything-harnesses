import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('bed running')
@cli.command()
def start(): click.echo('bed started')
if __name__ == '__main__': cli()
