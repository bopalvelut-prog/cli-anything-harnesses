import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('restore running')
@cli.command()
def start(): click.echo('restore started')
if __name__ == '__main__': cli()
