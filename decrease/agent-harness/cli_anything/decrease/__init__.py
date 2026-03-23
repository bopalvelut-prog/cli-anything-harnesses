import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('decrease running')
@cli.command()
def start(): click.echo('decrease started')
if __name__ == '__main__': cli()
