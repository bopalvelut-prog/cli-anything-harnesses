import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('regex running')
@cli.command()
def start(): click.echo('regex started')
if __name__ == '__main__': cli()
