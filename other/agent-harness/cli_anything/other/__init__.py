import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('other running')
@cli.command()
def start(): click.echo('other started')
if __name__ == '__main__': cli()
