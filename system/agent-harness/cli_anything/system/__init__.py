import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('system running')
@cli.command()
def start(): click.echo('system started')
if __name__ == '__main__': cli()
