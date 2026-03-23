import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('sovereign running')
@cli.command()
def start(): click.echo('sovereign started')
if __name__ == '__main__': cli()
