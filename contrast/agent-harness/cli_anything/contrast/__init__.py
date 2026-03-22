import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def scan(): click.echo('Contrast scan')
@cli.command()
def report(): click.echo('Contrast report')
if __name__ == '__main__': cli()
