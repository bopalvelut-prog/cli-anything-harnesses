import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('performance running')
@cli.command()
def start(): click.echo('performance started')
if __name__ == '__main__': cli()
