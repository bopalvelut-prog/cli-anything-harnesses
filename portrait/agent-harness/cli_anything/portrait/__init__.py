import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('portrait running')
@cli.command()
def start(): click.echo('portrait started')
if __name__ == '__main__': cli()
