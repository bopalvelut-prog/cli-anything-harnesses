import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('paste running')
@cli.command()
def start(): click.echo('paste started')
if __name__ == '__main__': cli()
