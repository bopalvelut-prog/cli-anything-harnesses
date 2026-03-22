import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def products(): click.echo('OpenCart products')
@cli.command()
def orders(): click.echo('OpenCart orders')
if __name__ == '__main__': cli()
