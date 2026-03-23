import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('others running')
@cli.command()
def start(): click.echo('others started')
if __name__ == '__main__': cli()
