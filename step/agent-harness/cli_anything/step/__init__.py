import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('step running')
@cli.command()
def start(): click.echo('step started')
if __name__ == '__main__': cli()
