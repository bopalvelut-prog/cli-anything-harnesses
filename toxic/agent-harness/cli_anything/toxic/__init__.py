import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('toxic running')
@cli.command()
def start(): click.echo('toxic started')
if __name__ == '__main__': cli()
