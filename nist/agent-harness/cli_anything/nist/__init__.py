import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('nist running')
@cli.command()
def start(): click.echo('nist started')
if __name__ == '__main__': cli()
