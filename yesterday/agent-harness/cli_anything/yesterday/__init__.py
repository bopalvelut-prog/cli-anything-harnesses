import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('yesterday running')
@cli.command()
def start(): click.echo('yesterday started')
if __name__ == '__main__': cli()
