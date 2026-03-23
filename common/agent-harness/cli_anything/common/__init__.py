import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('common running')
@cli.command()
def start(): click.echo('common started')
if __name__ == '__main__': cli()
