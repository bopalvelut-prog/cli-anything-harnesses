import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('extent running')
@cli.command()
def start(): click.echo('extent started')
if __name__ == '__main__': cli()
