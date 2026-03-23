import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('telephone running')
@cli.command()
def start(): click.echo('telephone started')
if __name__ == '__main__': cli()
