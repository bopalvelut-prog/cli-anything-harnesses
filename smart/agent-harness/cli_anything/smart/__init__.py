import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('smart running')
@cli.command()
def start(): click.echo('smart started')
if __name__ == '__main__': cli()
