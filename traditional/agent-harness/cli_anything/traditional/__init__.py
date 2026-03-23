import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('traditional running')
@cli.command()
def start(): click.echo('traditional started')
if __name__ == '__main__': cli()
