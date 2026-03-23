import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('docutils running')
@cli.command()
def start(): click.echo('docutils started')
if __name__ == '__main__': cli()
