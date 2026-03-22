import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def server(): subprocess.run(['rails', 'server'])
@cli.command()
def products(): click.echo('Spree products')
if __name__ == '__main__': cli()
