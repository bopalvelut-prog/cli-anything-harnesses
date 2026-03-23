import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('state running')
@cli.command()
def start(): click.echo('state started')
if __name__ == '__main__': cli()
