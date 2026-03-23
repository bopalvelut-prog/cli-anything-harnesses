import click
@click.group()
def cli(): pass
@cli.command()
def purge(): click.echo('MaxCDN purge')
@cli.command()
def zones(): click.echo('MaxCDN zones')
if __name__ == '__main__': cli()
