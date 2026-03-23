import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('augmented running')
@cli.command()
def start(): click.echo('augmented started')
if __name__ == '__main__': cli()
