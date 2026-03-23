import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('litestream running')
@cli.command()
def start(): click.echo('litestream started')
if __name__ == '__main__': cli()
