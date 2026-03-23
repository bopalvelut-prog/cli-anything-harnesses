import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('stream running')
@cli.command()
def start(): click.echo('stream started')
if __name__ == '__main__': cli()
