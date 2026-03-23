import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('friend running')
@cli.command()
def start(): click.echo('friend started')
if __name__ == '__main__': cli()
