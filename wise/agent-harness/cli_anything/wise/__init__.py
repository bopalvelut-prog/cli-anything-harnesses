import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('wise running')
@cli.command()
def start(): click.echo('wise started')
if __name__ == '__main__': cli()
