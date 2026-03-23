import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('relation running')
@cli.command()
def start(): click.echo('relation started')
if __name__ == '__main__': cli()
