import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('affinity running')
@cli.command()
def start(): click.echo('affinity started')
if __name__ == '__main__': cli()
