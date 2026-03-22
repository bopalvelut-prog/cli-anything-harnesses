import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def swap(): click.echo('1inch swap')
@cli.command()
def quote(): click.echo('1inch quote')
if __name__ == '__main__': cli()
