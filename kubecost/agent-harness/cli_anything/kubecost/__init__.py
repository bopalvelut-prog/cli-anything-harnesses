import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def cost(): click.echo('Kubecost analysis')
@cli.command()
def savings(): click.echo('Kubecost savings')
if __name__ == '__main__': cli()
