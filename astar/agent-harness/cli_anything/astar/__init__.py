import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def transfer(): click.echo('Astar transfer')
@cli.command()
def stake(): click.echo('Astar stake')
if __name__ == '__main__': cli()
