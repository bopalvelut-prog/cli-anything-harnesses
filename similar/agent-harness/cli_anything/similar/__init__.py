import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('similar running')
@cli.command()
def start(): click.echo('similar started')
if __name__ == '__main__': cli()
