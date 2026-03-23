import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('xcode running')
@cli.command()
def start(): click.echo('xcode started')
if __name__ == '__main__': cli()
