import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('ankr running')
@cli.command()
def start(): click.echo('ankr started')
if __name__ == '__main__': cli()
