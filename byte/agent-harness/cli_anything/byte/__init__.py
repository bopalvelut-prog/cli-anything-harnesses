import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('byte running')
@cli.command()
def start(): click.echo('byte started')
if __name__ == '__main__': cli()
