import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('succeed running')
@cli.command()
def start(): click.echo('succeed started')
if __name__ == '__main__': cli()
