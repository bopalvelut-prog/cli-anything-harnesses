import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('expose running')
@cli.command()
def start(): click.echo('expose started')
if __name__ == '__main__': cli()
