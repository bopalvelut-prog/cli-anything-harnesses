import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('beef running')
@cli.command()
def start(): click.echo('beef started')
if __name__ == '__main__': cli()
