import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('bucket running')
@cli.command()
def start(): click.echo('bucket started')
if __name__ == '__main__': cli()
