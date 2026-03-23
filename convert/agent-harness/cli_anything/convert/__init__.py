import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('convert running')
@cli.command()
def start(): click.echo('convert started')
if __name__ == '__main__': cli()
