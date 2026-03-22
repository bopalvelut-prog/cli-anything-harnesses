import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def start(): click.echo('AppFlowy started')
@cli.command()
def pages(): click.echo('AppFlowy pages')
if __name__ == '__main__': cli()
