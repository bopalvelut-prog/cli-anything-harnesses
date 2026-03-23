import click
@click.group()
def cli(): pass
@cli.command()
def purge(): click.echo('KeyCDN purge')
@cli.command()
def zones(): click.echo('KeyCDN zones')
if __name__ == '__main__': cli()
