import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('polynote running')
@cli.command()
def start(): click.echo('polynote started')
if __name__ == '__main__': cli()
