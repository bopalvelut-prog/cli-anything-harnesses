import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('madvr running')
@cli.command()
def start(): click.echo('madvr started')
if __name__ == '__main__': cli()
