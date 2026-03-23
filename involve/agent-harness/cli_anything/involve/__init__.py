import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('involve running')
@cli.command()
def start(): click.echo('involve started')
if __name__ == '__main__': cli()
