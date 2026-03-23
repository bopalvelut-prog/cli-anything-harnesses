import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('batch running')
@cli.command()
def start(): click.echo('batch started')
if __name__ == '__main__': cli()
