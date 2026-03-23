import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('query running')
@cli.command()
def start(): click.echo('query started')
if __name__ == '__main__': cli()
