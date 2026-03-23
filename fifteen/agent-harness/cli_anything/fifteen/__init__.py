import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('fifteen running')
@cli.command()
def start(): click.echo('fifteen started')
if __name__ == '__main__': cli()
