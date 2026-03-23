import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('musl running')
@cli.command()
def start(): click.echo('musl started')
if __name__ == '__main__': cli()
