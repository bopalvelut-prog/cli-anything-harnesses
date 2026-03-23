import click
@click.group()
def cli(): pass
@cli.command()
def purge(): click.echo('Fastly purge')
@cli.command()
def services(): click.echo('Fastly services')
if __name__ == '__main__': cli()
