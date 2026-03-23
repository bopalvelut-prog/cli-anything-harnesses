import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('mint running')
@cli.command()
def start(): click.echo('mint started')
if __name__ == '__main__': cli()
