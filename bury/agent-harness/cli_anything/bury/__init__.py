import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('bury running')
@cli.command()
def start(): click.echo('bury started')
if __name__ == '__main__': cli()
