import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('ftp running')
@cli.command()
def start(): click.echo('ftp started')
if __name__ == '__main__': cli()
