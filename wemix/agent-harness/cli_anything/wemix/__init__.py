import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def transfer(): click.echo('WEMIX transfer')
@cli.command()
def stake(): click.echo('WEMIX stake')
if __name__ == '__main__': cli()
