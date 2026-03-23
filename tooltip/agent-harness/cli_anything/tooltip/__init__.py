import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('tooltip running')
@cli.command()
def start(): click.echo('tooltip started')
if __name__ == '__main__': cli()
