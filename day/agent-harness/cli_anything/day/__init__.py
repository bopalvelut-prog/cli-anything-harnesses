import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('day running')
@cli.command()
def start(): click.echo('day started')
if __name__ == '__main__': cli()
