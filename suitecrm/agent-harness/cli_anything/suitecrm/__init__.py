import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def start(): click.echo('SuiteCRM started')
@cli.command()
def repair(): click.echo('SuiteCRM repair')
if __name__ == '__main__': cli()
