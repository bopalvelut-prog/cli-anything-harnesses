import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('since running')
@cli.command()
def start(): click.echo('since started')
if __name__ == '__main__': cli()
