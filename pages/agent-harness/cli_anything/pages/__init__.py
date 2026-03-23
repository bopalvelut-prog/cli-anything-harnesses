import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('pages running')
@cli.command()
def start(): click.echo('pages started')
if __name__ == '__main__': cli()
