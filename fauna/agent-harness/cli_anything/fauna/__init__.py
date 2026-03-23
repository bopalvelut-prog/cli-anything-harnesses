import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('fauna running')
@cli.command()
def start(): click.echo('fauna started')
if __name__ == '__main__': cli()
