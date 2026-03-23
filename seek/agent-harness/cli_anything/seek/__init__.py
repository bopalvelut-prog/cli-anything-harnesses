import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('seek running')
@cli.command()
def start(): click.echo('seek started')
if __name__ == '__main__': cli()
