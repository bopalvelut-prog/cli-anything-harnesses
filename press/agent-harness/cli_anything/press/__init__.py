import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('press running')
@cli.command()
def start(): click.echo('press started')
if __name__ == '__main__': cli()
