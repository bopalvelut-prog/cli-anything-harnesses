import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('consist running')
@cli.command()
def start(): click.echo('consist started')
if __name__ == '__main__': cli()
