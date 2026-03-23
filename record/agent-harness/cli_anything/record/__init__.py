import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('record running')
@cli.command()
def start(): click.echo('record started')
if __name__ == '__main__': cli()
