import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('original running')
@cli.command()
def start(): click.echo('original started')
if __name__ == '__main__': cli()
