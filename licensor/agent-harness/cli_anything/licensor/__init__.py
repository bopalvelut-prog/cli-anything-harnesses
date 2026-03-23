import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('licensor running')
@cli.command()
def start(): click.echo('licensor started')
if __name__ == '__main__': cli()
