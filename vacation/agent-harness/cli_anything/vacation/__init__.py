import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('vacation running')
@cli.command()
def start(): click.echo('vacation started')
if __name__ == '__main__': cli()
