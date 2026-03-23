import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('cake running')
@cli.command()
def start(): click.echo('cake started')
if __name__ == '__main__': cli()
