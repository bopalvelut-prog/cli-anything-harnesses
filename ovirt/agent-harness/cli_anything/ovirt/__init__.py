import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('ovirt running')
@cli.command()
def start(): click.echo('ovirt started')
if __name__ == '__main__': cli()
