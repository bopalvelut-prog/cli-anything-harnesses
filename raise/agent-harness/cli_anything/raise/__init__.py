import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('raise running')
@cli.command()
def start(): click.echo('raise started')
if __name__ == '__main__': cli()
