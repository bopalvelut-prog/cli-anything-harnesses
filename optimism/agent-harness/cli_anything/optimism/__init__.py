import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def node(): click.echo('Optimism node')
@cli.command()
def bridge(): click.echo('Optimism bridge')
if __name__ == '__main__': cli()
