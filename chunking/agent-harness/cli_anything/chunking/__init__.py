import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('chunking running')
@cli.command()
def start(): click.echo('chunking started')
if __name__ == '__main__': cli()
