import click
@click.group()
def cli(): pass
@cli.command()
def list(): click.echo('Firewalls')
@cli.command()
def create(): click.echo('Create firewall')
if __name__ == '__main__': cli()
