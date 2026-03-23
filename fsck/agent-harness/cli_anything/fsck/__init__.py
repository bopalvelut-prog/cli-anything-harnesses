import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('fsck running')
@cli.command()
def start(): click.echo('fsck started')
if __name__ == '__main__': cli()
