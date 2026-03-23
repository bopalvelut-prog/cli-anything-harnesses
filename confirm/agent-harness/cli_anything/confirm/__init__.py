import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('confirm running')
@cli.command()
def start(): click.echo('confirm started')
if __name__ == '__main__': cli()
