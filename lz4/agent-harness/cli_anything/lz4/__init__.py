import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('lz4 running')
@cli.command()
def start(): click.echo('lz4 started')
if __name__ == '__main__': cli()
