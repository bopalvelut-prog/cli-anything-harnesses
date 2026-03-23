import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('hope running')
@cli.command()
def start(): click.echo('hope started')
if __name__ == '__main__': cli()
