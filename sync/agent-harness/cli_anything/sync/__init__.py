import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('sync running')
@cli.command()
def start(): click.echo('sync started')
if __name__ == '__main__': cli()
