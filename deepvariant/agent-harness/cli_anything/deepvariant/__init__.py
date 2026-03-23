import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('deepvariant running')
@cli.command()
def start(): click.echo('deepvariant started')
if __name__ == '__main__': cli()
