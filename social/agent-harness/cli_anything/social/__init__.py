import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('social running')
@cli.command()
def start(): click.echo('social started')
if __name__ == '__main__': cli()
