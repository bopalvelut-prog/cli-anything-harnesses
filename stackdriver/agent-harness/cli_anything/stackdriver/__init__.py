import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('stackdriver running')
@cli.command()
def start(): click.echo('stackdriver started')
if __name__ == '__main__': cli()
