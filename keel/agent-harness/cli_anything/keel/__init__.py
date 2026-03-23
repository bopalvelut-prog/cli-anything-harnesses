import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('keel running')
@cli.command()
def start(): click.echo('keel started')
if __name__ == '__main__': cli()
