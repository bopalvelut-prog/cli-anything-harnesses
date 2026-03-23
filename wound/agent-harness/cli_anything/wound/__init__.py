import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('wound running')
@cli.command()
def start(): click.echo('wound started')
if __name__ == '__main__': cli()
