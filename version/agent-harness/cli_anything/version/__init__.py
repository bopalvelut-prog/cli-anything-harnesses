import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('version running')
@cli.command()
def start(): click.echo('version started')
if __name__ == '__main__': cli()
