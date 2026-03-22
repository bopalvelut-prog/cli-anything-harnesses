import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def mint(): click.echo('Immutable mint')
@cli.command()
def trade(): click.echo('Immutable trade')
if __name__ == '__main__': cli()
