import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('mine running')
@cli.command()
def start(): click.echo('mine started')
if __name__ == '__main__': cli()
