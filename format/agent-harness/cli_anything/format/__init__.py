import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('format running')
@cli.command()
def start(): click.echo('format started')
if __name__ == '__main__': cli()
