import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('duty running')
@cli.command()
def start(): click.echo('duty started')
if __name__ == '__main__': cli()
