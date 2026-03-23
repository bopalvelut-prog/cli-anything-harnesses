import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('hospital running')
@cli.command()
def start(): click.echo('hospital started')
if __name__ == '__main__': cli()
