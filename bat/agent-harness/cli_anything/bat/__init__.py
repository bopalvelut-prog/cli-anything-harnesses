import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('bat running')
@cli.command()
def start(): click.echo('bat started')
if __name__ == '__main__': cli()
