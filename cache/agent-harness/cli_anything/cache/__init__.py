import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('cache running')
@cli.command()
def start(): click.echo('cache started')
if __name__ == '__main__': cli()
