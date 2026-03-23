import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('weave running')
@cli.command()
def start(): click.echo('weave started')
if __name__ == '__main__': cli()
