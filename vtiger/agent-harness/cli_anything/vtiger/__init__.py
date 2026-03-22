import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def start(): click.echo('Vtiger started')
@cli.command()
def modules(): click.echo('Vtiger modules')
if __name__ == '__main__': cli()
