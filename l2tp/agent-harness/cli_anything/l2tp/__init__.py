import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('l2tp running')
@cli.command()
def start(): click.echo('l2tp started')
if __name__ == '__main__': cli()
