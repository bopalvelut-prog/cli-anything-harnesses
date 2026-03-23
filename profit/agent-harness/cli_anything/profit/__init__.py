import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('profit running')
@cli.command()
def start(): click.echo('profit started')
if __name__ == '__main__': cli()
