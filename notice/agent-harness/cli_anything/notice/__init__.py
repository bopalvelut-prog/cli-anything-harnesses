import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('notice running')
@cli.command()
def start(): click.echo('notice started')
if __name__ == '__main__': cli()
