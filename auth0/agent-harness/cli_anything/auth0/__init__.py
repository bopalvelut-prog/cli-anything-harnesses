import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('auth0 running')
@cli.command()
def start(): click.echo('auth0 started')
if __name__ == '__main__': cli()
