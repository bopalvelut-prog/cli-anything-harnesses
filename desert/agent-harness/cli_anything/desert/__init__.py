import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('desert running')
@cli.command()
def start(): click.echo('desert started')
if __name__ == '__main__': cli()
