import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('radical running')
@cli.command()
def start(): click.echo('radical started')
if __name__ == '__main__': cli()
