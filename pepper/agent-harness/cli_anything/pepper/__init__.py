import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('pepper running')
@cli.command()
def start(): click.echo('pepper started')
if __name__ == '__main__': cli()
