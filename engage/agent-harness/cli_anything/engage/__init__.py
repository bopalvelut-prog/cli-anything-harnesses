import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('engage running')
@cli.command()
def start(): click.echo('engage started')
if __name__ == '__main__': cli()
