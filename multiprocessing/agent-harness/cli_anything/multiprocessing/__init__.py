import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('multiprocessing running')
@cli.command()
def start(): click.echo('multiprocessing started')
if __name__ == '__main__': cli()
