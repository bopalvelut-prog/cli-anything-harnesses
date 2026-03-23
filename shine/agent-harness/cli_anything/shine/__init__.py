import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('shine running')
@cli.command()
def start(): click.echo('shine started')
if __name__ == '__main__': cli()
