import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('golang running')
@cli.command()
def start(): click.echo('golang started')
if __name__ == '__main__': cli()
