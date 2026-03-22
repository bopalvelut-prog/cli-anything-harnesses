import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def rooms(): click.echo('Element rooms')
@cli.command()
def send(): click.echo('Element message')
if __name__ == '__main__': cli()
