import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('slight running')
@cli.command()
def start(): click.echo('slight started')
if __name__ == '__main__': cli()
