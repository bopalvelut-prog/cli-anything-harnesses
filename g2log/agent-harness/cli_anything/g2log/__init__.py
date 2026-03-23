import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('g2log running')
@cli.command()
def start(): click.echo('g2log started')
if __name__ == '__main__': cli()
