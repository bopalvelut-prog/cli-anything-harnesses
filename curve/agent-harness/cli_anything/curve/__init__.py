import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('curve running')
@cli.command()
def start(): click.echo('curve started')
if __name__ == '__main__': cli()
