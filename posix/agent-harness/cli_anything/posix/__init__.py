import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('posix running')
@cli.command()
def start(): click.echo('posix started')
if __name__ == '__main__': cli()
