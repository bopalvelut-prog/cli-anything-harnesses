import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('set running')
@cli.command()
def start(): click.echo('set started')
if __name__ == '__main__': cli()
