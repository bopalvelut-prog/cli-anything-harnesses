import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('install running')
@cli.command()
def start(): click.echo('install started')
if __name__ == '__main__': cli()
