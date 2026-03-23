import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('artik running')
@cli.command()
def start(): click.echo('artik started')
if __name__ == '__main__': cli()
