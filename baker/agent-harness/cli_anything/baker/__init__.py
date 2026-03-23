import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('baker running')
@cli.command()
def start(): click.echo('baker started')
if __name__ == '__main__': cli()
