import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('vike running')
@cli.command()
def start(): click.echo('vike started')
if __name__ == '__main__': cli()
