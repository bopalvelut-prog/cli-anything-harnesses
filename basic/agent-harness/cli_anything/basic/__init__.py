import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('basic running')
@cli.command()
def start(): click.echo('basic started')
if __name__ == '__main__': cli()
