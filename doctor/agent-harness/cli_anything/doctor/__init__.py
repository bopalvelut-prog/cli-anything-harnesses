import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('doctor running')
@cli.command()
def start(): click.echo('doctor started')
if __name__ == '__main__': cli()
