import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('belong running')
@cli.command()
def start(): click.echo('belong started')
if __name__ == '__main__': cli()
