import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('citizen running')
@cli.command()
def start(): click.echo('citizen started')
if __name__ == '__main__': cli()
