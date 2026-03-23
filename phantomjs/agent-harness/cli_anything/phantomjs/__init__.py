import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('phantomjs running')
@cli.command()
def start(): click.echo('phantomjs started')
if __name__ == '__main__': cli()
