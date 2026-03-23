import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('zag running')
@cli.command()
def start(): click.echo('zag started')
if __name__ == '__main__': cli()
