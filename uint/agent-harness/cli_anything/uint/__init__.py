import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('uint running')
@cli.command()
def start(): click.echo('uint started')
if __name__ == '__main__': cli()
