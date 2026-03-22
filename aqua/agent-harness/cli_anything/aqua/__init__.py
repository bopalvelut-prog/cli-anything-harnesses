import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def scan(): click.echo('Aqua scan')
@cli.command()
def report(): click.echo('Aqua report')
if __name__ == '__main__': cli()
