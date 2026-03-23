import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('codesys running')
@cli.command()
def start(): click.echo('codesys started')
if __name__ == '__main__': cli()
