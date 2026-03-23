import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('special running')
@cli.command()
def start(): click.echo('special started')
if __name__ == '__main__': cli()
