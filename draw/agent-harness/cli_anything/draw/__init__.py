import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('draw running')
@cli.command()
def start(): click.echo('draw started')
if __name__ == '__main__': cli()
