import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('auto_scaling running')
@cli.command()
def start(): click.echo('auto_scaling started')
if __name__ == '__main__': cli()
