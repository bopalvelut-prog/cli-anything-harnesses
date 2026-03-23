import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('mirror running')
@cli.command()
def start(): click.echo('mirror started')
if __name__ == '__main__': cli()
