import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def start(): click.echo('Maltego started')
@cli.command()
def transforms(): click.echo('Available transforms')
if __name__ == '__main__': cli()
