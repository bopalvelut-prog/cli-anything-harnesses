import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('lunchy running')
@cli.command()
def start(): click.echo('lunchy started')
if __name__ == '__main__': cli()
