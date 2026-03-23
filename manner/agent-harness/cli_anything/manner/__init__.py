import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('manner running')
@cli.command()
def start(): click.echo('manner started')
if __name__ == '__main__': cli()
