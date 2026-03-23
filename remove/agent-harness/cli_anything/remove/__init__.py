import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('remove running')
@cli.command()
def start(): click.echo('remove started')
if __name__ == '__main__': cli()
