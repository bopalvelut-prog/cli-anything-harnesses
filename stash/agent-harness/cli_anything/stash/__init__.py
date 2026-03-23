import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('stash running')
@cli.command()
def start(): click.echo('stash started')
if __name__ == '__main__': cli()
