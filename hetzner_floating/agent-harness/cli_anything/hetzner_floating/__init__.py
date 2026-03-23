import click
@click.group()
def cli(): pass
@cli.command()
def list(): click.echo('Floating IPs')
@cli.command()
def create(): click.echo('Create floating IP')
if __name__ == '__main__': cli()
