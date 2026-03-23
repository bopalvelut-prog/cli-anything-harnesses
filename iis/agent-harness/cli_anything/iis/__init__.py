import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('iis running')
@cli.command()
def start(): click.echo('iis started')
if __name__ == '__main__': cli()
