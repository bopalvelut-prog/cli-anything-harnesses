import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('partner running')
@cli.command()
def start(): click.echo('partner started')
if __name__ == '__main__': cli()
