import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def trade(): click.echo('Perpetual trade')
@cli.command()
def position(): click.echo('Perpetual position')
if __name__ == '__main__': cli()
