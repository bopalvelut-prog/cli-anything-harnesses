import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('committee running')
@cli.command()
def start(): click.echo('committee started')
if __name__ == '__main__': cli()
