import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def transfer(): click.echo('Cronos transfer')
@cli.command()
def stake(): click.echo('Cronos stake')
if __name__ == '__main__': cli()
