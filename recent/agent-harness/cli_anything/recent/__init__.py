import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('recent running')
@cli.command()
def start(): click.echo('recent started')
if __name__ == '__main__': cli()
