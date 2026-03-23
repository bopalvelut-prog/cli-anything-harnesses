import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('proxy running')
@cli.command()
def start(): click.echo('proxy started')
if __name__ == '__main__': cli()
