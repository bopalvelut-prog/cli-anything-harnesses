import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('creative running')
@cli.command()
def start(): click.echo('creative started')
if __name__ == '__main__': cli()
