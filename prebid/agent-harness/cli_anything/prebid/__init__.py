import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('prebid running')
@cli.command()
def start(): click.echo('prebid started')
if __name__ == '__main__': cli()
