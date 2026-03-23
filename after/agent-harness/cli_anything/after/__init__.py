import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('after running')
@cli.command()
def start(): click.echo('after started')
if __name__ == '__main__': cli()
