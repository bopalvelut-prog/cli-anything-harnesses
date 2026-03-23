import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('canyon running')
@cli.command()
def start(): click.echo('canyon started')
if __name__ == '__main__': cli()
