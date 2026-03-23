import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('camp running')
@cli.command()
def start(): click.echo('camp started')
if __name__ == '__main__': cli()
