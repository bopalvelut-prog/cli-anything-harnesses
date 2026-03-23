import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('present running')
@cli.command()
def start(): click.echo('present started')
if __name__ == '__main__': cli()
