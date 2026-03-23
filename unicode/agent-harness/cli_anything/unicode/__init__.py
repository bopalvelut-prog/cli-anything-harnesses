import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('unicode running')
@cli.command()
def start(): click.echo('unicode started')
if __name__ == '__main__': cli()
