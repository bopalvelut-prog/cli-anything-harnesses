import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('left running')
@cli.command()
def start(): click.echo('left started')
if __name__ == '__main__': cli()
