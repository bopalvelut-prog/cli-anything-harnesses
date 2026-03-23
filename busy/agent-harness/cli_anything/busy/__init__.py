import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('busy running')
@cli.command()
def start(): click.echo('busy started')
if __name__ == '__main__': cli()
