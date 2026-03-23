import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('mineral running')
@cli.command()
def start(): click.echo('mineral started')
if __name__ == '__main__': cli()
