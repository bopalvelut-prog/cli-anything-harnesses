import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('enter running')
@cli.command()
def start(): click.echo('enter started')
if __name__ == '__main__': cli()
