import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('initial running')
@cli.command()
def start(): click.echo('initial started')
if __name__ == '__main__': cli()
