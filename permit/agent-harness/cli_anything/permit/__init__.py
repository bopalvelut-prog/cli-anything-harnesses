import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('permit running')
@cli.command()
def start(): click.echo('permit started')
if __name__ == '__main__': cli()
