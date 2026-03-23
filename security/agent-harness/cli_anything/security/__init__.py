import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('security running')
@cli.command()
def start(): click.echo('security started')
if __name__ == '__main__': cli()
