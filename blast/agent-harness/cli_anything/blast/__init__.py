import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('blast running')
@cli.command()
def start(): click.echo('blast started')
if __name__ == '__main__': cli()
