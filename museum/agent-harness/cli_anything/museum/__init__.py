import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('museum running')
@cli.command()
def start(): click.echo('museum started')
if __name__ == '__main__': cli()
