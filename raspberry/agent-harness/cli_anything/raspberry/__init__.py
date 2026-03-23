import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('raspberry running')
@cli.command()
def start(): click.echo('raspberry started')
if __name__ == '__main__': cli()
