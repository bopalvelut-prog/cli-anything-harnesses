import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('long running')
@cli.command()
def start(): click.echo('long started')
if __name__ == '__main__': cli()
