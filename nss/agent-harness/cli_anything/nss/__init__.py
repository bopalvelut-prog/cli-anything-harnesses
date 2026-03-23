import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('nss running')
@cli.command()
def start(): click.echo('nss started')
if __name__ == '__main__': cli()
