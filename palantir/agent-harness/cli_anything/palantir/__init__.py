import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('palantir running')
@cli.command()
def start(): click.echo('palantir started')
if __name__ == '__main__': cli()
