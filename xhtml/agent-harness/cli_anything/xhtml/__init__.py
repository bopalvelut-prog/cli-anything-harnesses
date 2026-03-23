import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('xhtml running')
@cli.command()
def start(): click.echo('xhtml started')
if __name__ == '__main__': cli()
