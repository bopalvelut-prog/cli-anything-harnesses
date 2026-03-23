import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('oci running')
@cli.command()
def start(): click.echo('oci started')
if __name__ == '__main__': cli()
