import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('magazine running')
@cli.command()
def start(): click.echo('magazine started')
if __name__ == '__main__': cli()
