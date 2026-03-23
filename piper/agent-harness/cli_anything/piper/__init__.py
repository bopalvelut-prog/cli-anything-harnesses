import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('piper running')
@cli.command()
def start(): click.echo('piper started')
if __name__ == '__main__': cli()
