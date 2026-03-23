import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('fail running')
@cli.command()
def start(): click.echo('fail started')
if __name__ == '__main__': cli()
