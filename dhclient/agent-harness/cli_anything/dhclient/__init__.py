import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('dhclient running')
@cli.command()
def start(): click.echo('dhclient started')
if __name__ == '__main__': cli()
