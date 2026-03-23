import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('bowl running')
@cli.command()
def start(): click.echo('bowl started')
if __name__ == '__main__': cli()
