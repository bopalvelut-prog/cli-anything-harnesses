import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('probe running')
@cli.command()
def start(): click.echo('probe started')
if __name__ == '__main__': cli()
