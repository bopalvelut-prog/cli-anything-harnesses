import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('xps running')
@cli.command()
def start(): click.echo('xps started')
if __name__ == '__main__': cli()
