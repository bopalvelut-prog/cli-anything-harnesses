import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('video running')
@cli.command()
def start(): click.echo('video started')
if __name__ == '__main__': cli()
