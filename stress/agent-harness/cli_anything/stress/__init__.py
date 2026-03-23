import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('stress running')
@cli.command()
def start(): click.echo('stress started')
if __name__ == '__main__': cli()
