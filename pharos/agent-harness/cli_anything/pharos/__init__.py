import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('pharos running')
@cli.command()
def start(): click.echo('pharos started')
if __name__ == '__main__': cli()
