import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('user running')
@cli.command()
def start(): click.echo('user started')
if __name__ == '__main__': cli()
