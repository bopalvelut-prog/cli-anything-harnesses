import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('working running')
@cli.command()
def start(): click.echo('working started')
if __name__ == '__main__': cli()
