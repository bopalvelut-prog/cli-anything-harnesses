import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('category running')
@cli.command()
def start(): click.echo('category started')
if __name__ == '__main__': cli()
