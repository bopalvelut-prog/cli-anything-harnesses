import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('child running')
@cli.command()
def start(): click.echo('child started')
if __name__ == '__main__': cli()
