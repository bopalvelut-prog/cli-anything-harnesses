import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def node(): click.echo('Horizen node')
@cli.command()
def wallet(): click.echo('Horizen wallet')
if __name__ == '__main__': cli()
