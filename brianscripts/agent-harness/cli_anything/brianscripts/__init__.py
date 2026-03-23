import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('brianscripts running')
@cli.command()
def start(): click.echo('brianscripts started')
if __name__ == '__main__': cli()
