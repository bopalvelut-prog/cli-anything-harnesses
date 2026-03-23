import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('dhcp running')
@cli.command()
def start(): click.echo('dhcp started')
if __name__ == '__main__': cli()
