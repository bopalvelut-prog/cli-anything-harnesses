import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('found running')
@cli.command()
def start(): click.echo('found started')
if __name__ == '__main__': cli()
