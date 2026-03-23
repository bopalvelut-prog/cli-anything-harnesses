import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('teach running')
@cli.command()
def start(): click.echo('teach started')
if __name__ == '__main__': cli()
