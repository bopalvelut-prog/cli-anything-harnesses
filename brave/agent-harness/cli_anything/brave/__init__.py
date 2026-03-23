import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('brave running')
@cli.command()
def start(): click.echo('brave started')
if __name__ == '__main__': cli()
