import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('pattern running')
@cli.command()
def start(): click.echo('pattern started')
if __name__ == '__main__': cli()
