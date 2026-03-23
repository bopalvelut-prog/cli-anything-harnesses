import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('sling running')
@cli.command()
def start(): click.echo('sling started')
if __name__ == '__main__': cli()
