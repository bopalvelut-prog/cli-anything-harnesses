import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('defrag running')
@cli.command()
def start(): click.echo('defrag started')
if __name__ == '__main__': cli()
