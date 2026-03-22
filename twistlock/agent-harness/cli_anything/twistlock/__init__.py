import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def scan(): click.echo('Twistlock scan')
@cli.command()
def report(): click.echo('Twistlock report')
if __name__ == '__main__': cli()
