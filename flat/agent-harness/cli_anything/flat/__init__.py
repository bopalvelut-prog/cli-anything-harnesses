import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('flat running')
@cli.command()
def start(): click.echo('flat started')
if __name__ == '__main__': cli()
