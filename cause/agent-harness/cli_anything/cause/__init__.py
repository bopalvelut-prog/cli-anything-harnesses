import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('cause running')
@cli.command()
def start(): click.echo('cause started')
if __name__ == '__main__': cli()
