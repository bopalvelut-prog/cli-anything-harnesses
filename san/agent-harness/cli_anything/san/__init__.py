import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('san running')
@cli.command()
def start(): click.echo('san started')
if __name__ == '__main__': cli()
