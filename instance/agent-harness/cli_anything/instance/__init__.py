import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('instance running')
@cli.command()
def start(): click.echo('instance started')
if __name__ == '__main__': cli()
