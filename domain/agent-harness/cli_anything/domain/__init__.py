import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('domain running')
@cli.command()
def start(): click.echo('domain started')
if __name__ == '__main__': cli()
