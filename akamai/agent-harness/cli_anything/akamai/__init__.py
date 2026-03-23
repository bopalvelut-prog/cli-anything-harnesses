import click
@click.group()
def cli(): pass
@cli.command()
def purge(): click.echo('Akamai purge')
@cli.command()
def properties(): click.echo('Akamai properties')
if __name__ == '__main__': cli()
