import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('tidy running')
@cli.command()
def start(): click.echo('tidy started')
if __name__ == '__main__': cli()
