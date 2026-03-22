import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def cost(): click.echo('OpenCost analysis')
if __name__ == '__main__': cli()
