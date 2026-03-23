import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('authelia running')
@cli.command()
def start(): click.echo('authelia started')
if __name__ == '__main__': cli()
