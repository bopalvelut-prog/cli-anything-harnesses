import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('trip running')
@cli.command()
def start(): click.echo('trip started')
if __name__ == '__main__': cli()
