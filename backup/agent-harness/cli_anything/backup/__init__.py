import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('backup running')
@cli.command()
def start(): click.echo('backup started')
if __name__ == '__main__': cli()
