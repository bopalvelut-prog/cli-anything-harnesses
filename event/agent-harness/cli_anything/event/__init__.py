import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('event running')
@cli.command()
def start(): click.echo('event started')
if __name__ == '__main__': cli()
