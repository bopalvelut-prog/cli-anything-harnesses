import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def trade(): click.echo('Loopring trade')
@cli.command()
def transfer(): click.echo('Loopring transfer')
if __name__ == '__main__': cli()
