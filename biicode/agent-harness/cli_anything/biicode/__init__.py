import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('biicode running')
@cli.command()
def start(): click.echo('biicode started')
if __name__ == '__main__': cli()
