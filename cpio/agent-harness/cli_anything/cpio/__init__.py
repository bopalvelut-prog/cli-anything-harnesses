import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('cpio running')
@cli.command()
def start(): click.echo('cpio started')
if __name__ == '__main__': cli()
