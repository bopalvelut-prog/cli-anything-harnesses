import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('argilla running')
@cli.command()
def start(): click.echo('argilla started')
if __name__ == '__main__': cli()
