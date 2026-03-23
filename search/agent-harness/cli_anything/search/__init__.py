import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('search running')
@cli.command()
def start(): click.echo('search started')
if __name__ == '__main__': cli()
