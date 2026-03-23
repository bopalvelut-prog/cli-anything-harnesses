import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('pmd running')
@cli.command()
def start(): click.echo('pmd started')
if __name__ == '__main__': cli()
