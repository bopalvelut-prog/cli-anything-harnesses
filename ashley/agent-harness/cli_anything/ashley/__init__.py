import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('ashley running')
@cli.command()
def start(): click.echo('ashley started')
if __name__ == '__main__': cli()
