import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('jelly running')
@cli.command()
def start(): click.echo('jelly started')
if __name__ == '__main__': cli()
