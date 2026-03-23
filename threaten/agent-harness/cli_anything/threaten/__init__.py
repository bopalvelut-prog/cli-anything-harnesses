import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('threaten running')
@cli.command()
def start(): click.echo('threaten started')
if __name__ == '__main__': cli()
