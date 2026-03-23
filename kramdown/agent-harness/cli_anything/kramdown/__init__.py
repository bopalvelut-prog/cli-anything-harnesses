import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('kramdown running')
@cli.command()
def start(): click.echo('kramdown started')
if __name__ == '__main__': cli()
