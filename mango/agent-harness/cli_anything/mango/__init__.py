import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('mango running')
@cli.command()
def start(): click.echo('mango started')
if __name__ == '__main__': cli()
