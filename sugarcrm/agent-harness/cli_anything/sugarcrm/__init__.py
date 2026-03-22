import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def start(): click.echo('SugarCRM started')
@cli.command()
def repair(): click.echo('SugarCRM repair')
if __name__ == '__main__': cli()
