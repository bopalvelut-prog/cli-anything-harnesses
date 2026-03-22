import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def trade(): click.echo('Synthetix trade')
@cli.command()
def stake(): click.echo('Synthetix stake')
if __name__ == '__main__': cli()
