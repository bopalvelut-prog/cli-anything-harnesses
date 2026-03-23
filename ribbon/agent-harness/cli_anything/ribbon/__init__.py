import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('ribbon running')
@cli.command()
def start(): click.echo('ribbon started')
if __name__ == '__main__': cli()
