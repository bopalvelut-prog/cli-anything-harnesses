import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('hotwire running')
@cli.command()
def start(): click.echo('hotwire started')
if __name__ == '__main__': cli()
