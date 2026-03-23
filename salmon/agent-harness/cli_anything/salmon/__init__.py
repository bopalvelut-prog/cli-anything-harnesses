import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('salmon running')
@cli.command()
def start(): click.echo('salmon started')
if __name__ == '__main__': cli()
