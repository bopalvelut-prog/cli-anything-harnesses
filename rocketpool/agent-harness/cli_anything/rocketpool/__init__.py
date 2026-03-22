import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def stake(): click.echo('Rocket Pool stake')
@cli.command()
def node(): click.echo('Rocket Pool node')
if __name__ == '__main__': cli()
