import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('preview running')
@cli.command()
def start(): click.echo('preview started')
if __name__ == '__main__': cli()
