import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('wav running')
@cli.command()
def start(): click.echo('wav started')
if __name__ == '__main__': cli()
