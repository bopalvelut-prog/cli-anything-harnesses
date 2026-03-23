import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('leadership running')
@cli.command()
def start(): click.echo('leadership started')
if __name__ == '__main__': cli()
