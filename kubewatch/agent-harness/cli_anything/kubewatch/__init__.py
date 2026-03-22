import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def watch(): click.echo('KubeWatch watching')
if __name__ == '__main__': cli()
