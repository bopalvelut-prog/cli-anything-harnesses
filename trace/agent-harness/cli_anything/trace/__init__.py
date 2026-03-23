import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('trace running')
@cli.command()
def start(): click.echo('trace started')
if __name__ == '__main__': cli()
