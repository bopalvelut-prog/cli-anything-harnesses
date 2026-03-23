import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('unmount running')
@cli.command()
def start(): click.echo('unmount started')
if __name__ == '__main__': cli()
