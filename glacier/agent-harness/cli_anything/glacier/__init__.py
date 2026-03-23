import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('glacier running')
@cli.command()
def start(): click.echo('glacier started')
if __name__ == '__main__': cli()
