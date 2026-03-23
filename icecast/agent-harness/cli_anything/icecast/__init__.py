import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('icecast running')
@cli.command()
def start(): click.echo('icecast started')
if __name__ == '__main__': cli()
