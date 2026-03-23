import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('relative running')
@cli.command()
def start(): click.echo('relative started')
if __name__ == '__main__': cli()
