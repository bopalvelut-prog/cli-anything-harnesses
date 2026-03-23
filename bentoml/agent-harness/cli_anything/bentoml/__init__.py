import click
@click.group()
def cli(): pass
@cli.command()
def serve(): click.echo('BentoML serve')
@cli.command()
def build(): click.echo('BentoML build')
if __name__ == '__main__': cli()
