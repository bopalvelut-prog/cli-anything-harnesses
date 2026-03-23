import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('xunit running')
@cli.command()
def start(): click.echo('xunit started')
if __name__ == '__main__': cli()
