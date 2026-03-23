import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('web running')
@cli.command()
def start(): click.echo('web started')
if __name__ == '__main__': cli()
