import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('pylance running')
@cli.command()
def start(): click.echo('pylance started')
if __name__ == '__main__': cli()
