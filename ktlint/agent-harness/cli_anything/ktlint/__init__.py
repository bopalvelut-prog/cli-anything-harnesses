import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('ktlint running')
@cli.command()
def start(): click.echo('ktlint started')
if __name__ == '__main__': cli()
