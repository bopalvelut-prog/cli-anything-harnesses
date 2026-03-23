import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('udev running')
@cli.command()
def start(): click.echo('udev started')
if __name__ == '__main__': cli()
