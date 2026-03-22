import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def node(): click.echo('BSC node')
@cli.command()
def bridge(): click.echo('BSC bridge')
if __name__ == '__main__': cli()
