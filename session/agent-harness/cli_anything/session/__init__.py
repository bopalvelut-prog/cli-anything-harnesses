import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('session running')
@cli.command()
def start(): click.echo('session started')
if __name__ == '__main__': cli()
