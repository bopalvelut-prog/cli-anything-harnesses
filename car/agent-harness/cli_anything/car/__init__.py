import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('car running')
@cli.command()
def start(): click.echo('car started')
if __name__ == '__main__': cli()
