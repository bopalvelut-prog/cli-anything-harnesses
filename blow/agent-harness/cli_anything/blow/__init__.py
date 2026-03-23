import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('blow running')
@cli.command()
def start(): click.echo('blow started')
if __name__ == '__main__': cli()
