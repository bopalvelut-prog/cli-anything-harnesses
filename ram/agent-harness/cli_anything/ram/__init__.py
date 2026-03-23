import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('ram running')
@cli.command()
def start(): click.echo('ram started')
if __name__ == '__main__': cli()
