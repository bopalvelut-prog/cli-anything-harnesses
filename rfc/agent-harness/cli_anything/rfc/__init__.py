import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('rfc running')
@cli.command()
def start(): click.echo('rfc started')
if __name__ == '__main__': cli()
