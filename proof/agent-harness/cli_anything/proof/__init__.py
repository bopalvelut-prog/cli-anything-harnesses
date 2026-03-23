import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('proof running')
@cli.command()
def start(): click.echo('proof started')
if __name__ == '__main__': cli()
