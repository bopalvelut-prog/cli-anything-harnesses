import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('pdb running')
@cli.command()
def start(): click.echo('pdb started')
if __name__ == '__main__': cli()
