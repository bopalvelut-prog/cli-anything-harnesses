import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('know running')
@cli.command()
def start(): click.echo('know started')
if __name__ == '__main__': cli()
