import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('website running')
@cli.command()
def start(): click.echo('website started')
if __name__ == '__main__': cli()
