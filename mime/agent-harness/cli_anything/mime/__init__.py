import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('mime running')
@cli.command()
def start(): click.echo('mime started')
if __name__ == '__main__': cli()
