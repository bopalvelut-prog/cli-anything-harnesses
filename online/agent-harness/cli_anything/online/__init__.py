import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('online running')
@cli.command()
def start(): click.echo('online started')
if __name__ == '__main__': cli()
