import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('kpatch running')
@cli.command()
def start(): click.echo('kpatch started')
if __name__ == '__main__': cli()
