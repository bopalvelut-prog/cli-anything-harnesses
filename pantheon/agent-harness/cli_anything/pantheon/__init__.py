import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('pantheon running')
@cli.command()
def start(): click.echo('pantheon started')
if __name__ == '__main__': cli()
