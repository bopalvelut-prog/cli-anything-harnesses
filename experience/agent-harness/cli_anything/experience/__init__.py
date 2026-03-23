import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('experience running')
@cli.command()
def start(): click.echo('experience started')
if __name__ == '__main__': cli()
