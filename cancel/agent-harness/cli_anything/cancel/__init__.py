import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('cancel running')
@cli.command()
def start(): click.echo('cancel started')
if __name__ == '__main__': cli()
