import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('keep running')
@cli.command()
def start(): click.echo('keep started')
if __name__ == '__main__': cli()
