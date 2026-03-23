import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('osx running')
@cli.command()
def start(): click.echo('osx started')
if __name__ == '__main__': cli()
