import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('acuity running')
@cli.command()
def start(): click.echo('acuity started')
if __name__ == '__main__': cli()
