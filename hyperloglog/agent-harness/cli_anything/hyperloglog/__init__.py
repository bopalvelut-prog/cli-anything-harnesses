import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('hyperloglog running')
@cli.command()
def start(): click.echo('hyperloglog started')
if __name__ == '__main__': cli()
