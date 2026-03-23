import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('giant running')
@cli.command()
def start(): click.echo('giant started')
if __name__ == '__main__': cli()
