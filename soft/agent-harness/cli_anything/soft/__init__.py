import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('soft running')
@cli.command()
def start(): click.echo('soft started')
if __name__ == '__main__': cli()
